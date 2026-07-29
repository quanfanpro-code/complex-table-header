from __future__ import annotations

import argparse
from pathlib import Path


项目根目录 = Path(__file__).resolve().parents[1]
技能文件 = 项目根目录 / "SKILL.md"

必需内容 = {
    "foundation": [
        "帮助AI识别表格本身",
        "## 成功标准",
        "## 核心原则",
        "## 快速识别主流程",
        "盘点证据",
        "验证并输出",
    ],
    "structure": [
        "## 统一表格对象模型",
        "表格区块",
        "结构格",
        "跨格关系",
        "结构性空白",
        "二维递归切块",
        "原始结构",
        "展开视图",
    ],
    "relationships": [
        "## 单元格角色",
        "列表头",
        "行表头",
        "角部表头",
        "分组标题",
        "数据格",
        "表头关系",
        "作用范围",
        "重复表头",
    ],
    "uncertainty": [
        "## 歧义与停止强猜",
        "候选结构",
        "冲突证据",
        "停止强猜",
        "数据表格",
        "表单式表格",
        "排版容器",
        "混合结构",
        "## 验证清单",
    ],
}

禁止内容 = [
    "超过60%",
    "超过70%",
    "兜底默认1行",
    "第一行文本，其余表格",
]


def 检查(分组: str) -> list[str]:
    原始字节 = 技能文件.read_bytes()
    文本 = 原始字节.decode("utf-8-sig")
    错误: list[str] = []

    if not 原始字节.startswith(b"\xef\xbb\xbf"):
        错误.append("SKILL.md不是UTF-8 with BOM")
    if "\ufffd" in 文本:
        错误.append("存在Unicode替换字符")
    if chr(63) in 文本:
        错误.append("存在英文问号，需排查中文降级")
    if "name: complex-table-header" not in 文本:
        错误.append("技能名称缺失")

    检查分组 = 必需内容 if 分组 == "all" else {分组: 必需内容[分组]}
    for 名称, 词语列表 in 检查分组.items():
        for 词语 in 词语列表:
            if 词语 not in 文本:
                错误.append(f"{名称}缺少：{词语}")

    if 分组 == "all":
        for 词语 in 禁止内容:
            if 词语 in 文本:
                错误.append(f"仍含危险旧规则：{词语}")

    return 错误


def main() -> int:
    parser = argparse.ArgumentParser(description="检查复杂表格识别技能的机械契约")
    parser.add_argument(
        "--group",
        choices=[*必需内容, "all"],
        default="all",
        help="只检查指定规则组",
    )
    参数 = parser.parse_args()
    错误 = 检查(参数.group)
    if 错误:
        for 项目 in 错误:
            print(f"FAIL: {项目}")
        return 1
    print(f"PASS: {参数.group}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

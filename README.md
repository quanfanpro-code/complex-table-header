# 复杂表格识别技能（complex-table-header）

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

帮助 AI 识别复杂表格本身：先判断哪里是真正的表格，再恢复表格区块、行、列、单元格、跨格、角色和表头关系。

适用于多级表头、跨格、行列分组、嵌套、续表、表单或结构歧义等场景。支持 Excel、Word、PDF、扫描件、图片、网页或纯文本等多种载体。

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 技能定义：识别流程、证据规则、输出要求 |
| `CONTEXT.md` | 领域上下文：核心对象与术语定义 |
| `test-prompts.json` | 测试用例 |
| `tests/validate_skill.py` | 技能验证脚本 |

## 使用方式

将 `SKILL.md` 和 `CONTEXT.md` 加载到 AI 助手的技能系统中即可使用。详见 `SKILL.md` 中的完整说明。

## 开源协议

本项目基于 [**GNU AGPL v3.0**](LICENSE) 协议开源。

- ✅ 可以自由使用、修改、分发
- ✅ 可以用于商业用途
- ⚠️ 必须保留原始协议声明
- ⚠️ 必须公开修改后的源代码
- ⚠️ 必须以相同的 AGPL v3.0 协议发布衍生作品
- ⚠️ 如果通过网络提供服务，也必须公开源代码

详见 [LICENSE](LICENSE) 文件。

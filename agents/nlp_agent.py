
def parse_query(query: str):
    # 模拟 LLM 输出（真实可接 OpenAI）
    if "区域" in query:
        return {
            "group_by": ["Region"],
            "metrics": ["Sales"]
        }
    return {
        "group_by": [],
        "metrics": ["Sales"]
    }

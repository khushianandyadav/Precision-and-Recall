def calculate_metrics(answer_set,relevant_set):
    tp = len(answer_set & relevant_set)
    precision = tp / len(answer_set) if answer_set else 0
    recall = tp / len(relevant_set) if relevant_set else 0
    return precision, recall

def main():
    queries = {
        "q1": {
            "answer_set": {"D1, D2, D4, D6"},
            "relevant_set": {"D2", "D3", "D4", "D5"}
        },
        "q2": {
            "answer_set": {"D3", "D5", "D7"},
            "relevant_set": {"D5", "D6", "D7", "D8"}
        },
        "q3": {
            "answer_set": {"D10", "D11"},
            "relevant_set": {"D9", "D10", "D11", "D12"}
        }
    }

    print("Multiple Queries")
    for query_id, data in queries.items():
        p, r = calculate_metrics(data["answer_set"], data["relevant_set"])
        print(f"\nQuery: {query_id}")
        print(f"    Precision:  {p:.2f}")
        print(f"    Recall:     {r:.2f}")


if __name__ == '__main__':
    main()
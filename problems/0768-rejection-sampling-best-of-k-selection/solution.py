def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """
    selected_candidates = []
    n = len(candidates)
    for i in range(n):
        arr = candidates[i]
        score = scores[i]
        idx = score.index(max(score))
        selected_candidates.append(arr[idx])
    return selected_candidates

function solution(cards1, cards2, goal) {
    cards1 = cards1.reverse();
    cards2 = cards2.reverse();

    for (i of goal) {
        if (cards1[cards1.length - 1] == i) {
            cards1.pop();

        } else if (cards2[cards2.length - 1] == i) {
            cards2.pop();

        } else {
            return "No";
        }
    }

    return "Yes";
}
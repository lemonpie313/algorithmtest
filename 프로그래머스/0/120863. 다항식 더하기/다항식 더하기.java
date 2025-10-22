class Solution {
    public String solution(String polynomial) {
        String[] polynomialArray = polynomial.split(" \\+ ");
        String num;
        int number = 0;
        int numberx = 0;
        for (String a:polynomialArray) {
            if (a.contains("x")) {
                num = a.substring(0, a.length() -1);
                if (num.isEmpty()) {
                    numberx += 1;
                } else {
                    numberx += Integer.parseInt(num);
                }
                
            } else {
                num = a;
                number += Integer.parseInt(num);
            }
        }
        if (numberx == 0) {
            return Integer.toString(number);
        } else if (number == 0) {
            if (numberx == 1) {
                return "x";
            }
            return Integer.toString(numberx) + "x";
        } else if (numberx == 1) {
            return "x + " + number;
        }
        return numberx + "x + " + number;
    }
}
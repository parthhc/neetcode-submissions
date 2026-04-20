class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sAsChars = s.toCharArray();
        char[] tAsChars = t.toCharArray();

        HashMap<Character, Integer> seenCharsS = new HashMap<>();
        HashMap<Character, Integer> seenCharsT = new HashMap<>();

        for (int i = 0; i < sAsChars.length; i++) {
            if (seenCharsS.containsKey(sAsChars[i])) {
                seenCharsS.put(sAsChars[i], seenCharsS.get(sAsChars[i]) + 1);
            } else {
                seenCharsS.put(sAsChars[i], 0);
            }
        }

        for (int i = 0; i < tAsChars.length; i++) {
            if (seenCharsT.containsKey(tAsChars[i])) {
                seenCharsT.put(tAsChars[i], seenCharsT.get(tAsChars[i]) + 1);
            } else {
                seenCharsT.put(tAsChars[i], 0);
            }
        }

        if (seenCharsS.equals(seenCharsT)) {
            return true;
        }
        return false;



    }
}

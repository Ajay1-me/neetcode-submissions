class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        //converts string into character array
        char[] arr1 = s.toCharArray();
        char[] arr2 = t.toCharArray();

        //sort characters in the arrays 
        Arrays.sort(arr1);
        Arrays.sort(arr2);

        //returns true if the sorted arrays are the same, false otherwise 
        return Arrays.equals(arr1, arr2);

    }
}

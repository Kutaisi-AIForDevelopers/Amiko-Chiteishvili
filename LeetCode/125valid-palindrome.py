class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ""

        for char in s:
            if char.isalnum():
                cleaned_text += char.lower()

        if cleaned_text == cleaned_text[::-1]:
            return True
        else:
            return False
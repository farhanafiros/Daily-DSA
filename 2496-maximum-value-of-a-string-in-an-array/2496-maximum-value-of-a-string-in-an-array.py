class Solution:
    def maximumValue(self, strs: List[str]) -> int:
      max_value =0
      for i in strs:
        if i.isdigit():
            max_value = max(max_value,int(i))
        else:
            max_value = max(max_value,len(i))
      return max_value

        
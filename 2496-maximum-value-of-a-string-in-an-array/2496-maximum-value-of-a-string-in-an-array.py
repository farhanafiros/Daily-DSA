class Solution:
    def maximumValue(self, strs: List[str]) -> int:
      max_value =0 
      for i in strs:
        if i.isdigit():
            if max_value < int(i):
                max_value = int (i)
        else:
            if max_value <len(i):
                max_value = len(i)
      return max_value

        
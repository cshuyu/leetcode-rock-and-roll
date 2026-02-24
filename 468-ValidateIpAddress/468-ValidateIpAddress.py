# Last updated: 2/23/2026, 6:47:03 PM
class Solution:
    def isIpV4(self, elements: List[str]) -> bool:
        if len(elements) != 4:
            return False
        print(elements)
        for element in elements:
            if not element or len(element) > 3:
                return False
            length = len(element)
            total_val = 0
            for i in range(length):
                c = element[i]
                v = ord(c)
                if c == '0' and i == 0 and length > 1:
                    return False
                if v < ord('0') or v > ord('9'):
                    return False
                total_val = total_val * 10 + v - ord('0')
            if total_val > 255:
                return False
        return True
                    
    def isIpV6(self, elements: List[str]) -> bool:
        if len(elements) != 8:
            return False
        for element in elements:
            if not element or len(element) > 4:
                return False
            length = len(element)
            for i in range(length):
                c = element[i]
                v = ord(c)
                if (v >= ord('0') and v <= ord('9')) or (v >= ord('a') and v <= ord('f')) or (v >= ord('A') and v <= ord('F')):
                    continue
                else:
                    return False
        return True


    def validIPAddress(self, queryIP: str) -> str:
        isIpV4 = None
        isIpV6 = None
        cnt = 0
        
        elements = queryIP.split(':')
        if len(elements) == 8:
            if self.isIpV6(elements):
                return 'IPv6'
            else:
                return 'Neither'
        
        elements = queryIP.split('.')
        if len(elements) == 4:
            if self.isIpV4(elements):
                return 'IPv4'
            else:
                return 'Neither'

        return 'Neither'     
                    
                
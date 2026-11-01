class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        n = len(num)
        ans = []

        def solve(start, curr, sumi, ln):
            if start == n:
                if sumi == target:
                    ans.append("".join(curr.copy()))
                return

            for end in range(start, n):
                sub = num[start:end+1]

                if len(sub) > 1 and sub[0] == "0":
                    break

                val = int(sub)

                curr.append("+")
                curr.append(sub)
                solve(end+1, curr, sumi + val, val)
                curr.pop()
                curr.pop()

                curr.append("-")
                curr.append(sub)
                solve(end+1, curr, sumi - val, -val)
                curr.pop()
                curr.pop()

                curr.append("*")
                curr.append(sub)
                solve(end+1, curr, sumi - ln + val * ln, val * ln)
                curr.pop()
                curr.pop()

        for end in range(n):
            sub = num[:end+1]

            if len(sub) > 1 and sub[0] == "0":
                break

            solve(end+1, [sub], int(sub), int(sub))

        return ans
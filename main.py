def solve(n, m, records):
    pts = 0
    str_check = []
    intel_check = []
    
    for r in records:
        if r == 0:
            pts += 1  
        elif r > 0:
            intel_check.append(r)  
        else:
            str_check.append(-r)  
    
    intel_check.sort()
    str_check.sort()
    
    def pass_check(prefer_str):
        local_str = 0
        local_intel = 0
        local_pts = 0
        check_passed = 0
        
        for r in records:
            if r == 0:
                local_pts += 1  
            elif r > 0:
                if local_intel >= r:
                    check_passed += 1  
                elif local_pts > 0 and not prefer_str:
                    pts_needed = r - local_intel
                    if local_pts >= pts_needed:
                        local_pts -= pts_needed
                        local_intel = r
                        check_passed += 1
            else:
                if local_str >= -r:
                    check_passed += 1  
                elif local_pts > 0 and prefer_str:
                    pts_needed = -r - local_str
                    if local_pts >= pts_needed:
                        local_pts -= pts_needed
                        local_str = -r
                        check_passed += 1
        
        return check_passed

    result_str_first = pass_check(True)
    result_intel_first = pass_check(False)

    return max(result_str_first, result_intel_first)

n,m = map(int, input().split())  
r =  input().split()
r = [int(x) for x in r]

print(solve(n,m,r))

LL1 = [0.38629458881243667, 0.348416128261918, 0.35083062713812385, 0.3397494258886716, 0.3709808184869573, 0.39020154084630854,0.7754660433212932,  0.868459975386581]
LL_FA1 = [0.384, 0.31580788583017466, 0.3496888579258091, 0.3305227569851049, 0.3415928548086491, 0.3935968944947872, 0.771, 0.742]

def r44(value): return f"{round(value, 3):.3f}"


LL2 = [0.390, 0.350, 0.353, 0.344, 0.364, 0.386, 0.785, 0.860]
LL_FA2 = [0.380, 0.319, 0.340, 0.341, 0.347, 0.391, 0.771, 0.742]

mean_LL = [(ll1 + ll2) / 2 for ll1, ll2 in zip(LL1, LL2)]
mean_LL_FA = [(ll_fa1 + ll_fa2) / 2 for ll_fa1, ll_fa2 in zip(LL_FA1, LL_FA2)]

print('&'.join([r44(i) for i in mean_LL]))

def tolatx(ref, obj):
    res = ''
    for i,j in zip(ref,obj):
        if j == '-':
            res += '-&'
            continue
        a = min(int(max(0, i-j)*10000),100)
        if a != 0:
            a = max(a,20)
        b = '\dec{'+str(a)+'}{'+r44(j)+'}&'
        res += b
    return res[:-1]
print(tolatx(mean_LL, mean_LL_FA))
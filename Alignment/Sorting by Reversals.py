import collections

def get_all_permutations(s): # 起生成器作用的函数，作用是依次生成排列
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            yield (s[:i] + s[i:j][::-1] + s[j:],[i,j])


def get_reversal_distance(p1, p2): # 计算翻转距离的函数
    if p1 == p2: # 如果两个排列相等，可以直接返回翻转距离为0
        return 0

    target = tuple(p2) # 排列p2作为翻转的目标排列
    fromfirst = {tuple(p1): [0,[]]} # 创建字典，key为排列，value为初始排列翻转几次能得到该排列，先把p1放进去
    q = collections.deque((p1,)) # deque是一种数据对象，类似列表，但插入和删除的效率更高。创建这么一个对象q，                                                          #并把p1放进去。不难发现，q中数据是按翻转次数排列的。


    while len(q): # 如果q中还有排列，就继续循环
        s = tuple(q.popleft()) # 把q中第一个排列移除，放到s中
        c = fromfirst[s][0] # 从字典中查出来该排列对应的翻转次数
        _ind_ = fromfirst[s][1]
        for j,ind in get_all_permutations(s): # j接受生成器产生的排列
            if j == target: # 如果新产生的排列和目标排列相同，意味着最小翻转次数找到了，就可以把次数直接返回输出了
                return [c + 1,_ind_+ind]

            if not j in fromfirst: # 如果排列还不在字典里，把它添加进去
                fromfirst[j] = [c + 1,_ind_+ind]

                if c != 4: # 如果翻转已经超过5次了，就先停止，不再记录次数更多的排列
                    q.append(j)

    # 如果之前的5次翻转都没翻转出目标排列，就从另一头开始
    fromsecond = {tuple(p2): [0,[]]} # 创建新的字典，key为排列，value为初始排列翻转几次能得到该排列，把p2放进去
    target = tuple(p1) # 这次以排列p1作为翻转的目标排列
    q = collections.deque((p2,)) # 把p2排列放进q
    answer = 100000
    res_ind = [0] * 100000
    while len(q): # 和上个翻转循环过程含义相同，这次翻转不超过4次
        s = tuple(q.popleft())
        c = fromsecond[s][0]
        _ind_ = fromsecond[s][1]
        if c == 4:
            break

        for j,ind in get_all_permutations(s):
            if j == target:# 如果新产生的排列和目标排列相同，意味着最小翻转次数找到了，就可以把次数直接返回输出了
                return [c + 1,_ind_+ind]

            if not j in fromsecond:
                fromsecond[j] = [c + 1,_ind_+ind]

                if c != 3:
                    q.append(j)

            if j in fromfirst: # p2经过翻转和第一次翻转循环产生的某个排列相同
                answer = min(answer, fromfirst[j][0] + fromsecond[j][0]) # 把两次翻转的次数相加即为最终结果
                if len(res_ind) > len(fromfirst[j][1] + fromsecond[j][1]):
                    res_ind = fromfirst[j][1] + rev(fromsecond[j][1])
    return answer,res_ind
def rev(lst):
    res = []
    for i in range(0,len(lst),2):
        res.insert(0,lst[i])
        res.insert(1,lst[i+1])
    return res
with open("D:/Download/rosalind_sort.txt",mode='r') as f: #rosalind_sort
    s1,s2 = [i.strip('\n').split() for i in f.readlines()]

times , route = get_reversal_distance(s1,s2)
print(times)
for i in range(0,len(route),2):
    print(route[i]+1,route[i+1])
import multiprocessing as mp
mp = mp.get_context('spawn')
pool = []
n_proc = 2  # 开4进程
target_loc = [(i,i+1) for i in range(1000)]
total_num = len(target_loc)
phrase = total_num // n_proc + 1
import time
def func_plus(d, aa,no):
    # time.sleep(1)
    print(no)
    ss = []
    for a in aa:
        t1, t2 = a
        ss.append(t1+t2)
    d[no] = ss
    return ss
def just_run():
    with mp.Manager() as manger: # 由 Manager() 返回的管理器对象控制一个服务进程，该进程保存Python对象并允许其他进程使用代理操作它们。
        d = manger.dict()
        for i in range(n_proc):
            divied_target = target_loc[i*phrase:(i+1)*phrase]  # 所有的数据分成n_proc份
            process = mp.Process(target=func_plus, args=(d, divied_target,i))
            # 每个进程都执行prediction_by_dfsd
            process.start()
            pool.append(process)
            process.join()
        for p in pool:
            print(p)
        print(d)
# for p in pool: d
#     p.join()  # 等待所有进程执行完毕
# https://docs.python.org/zh-cn/3/library/multiprocessing.html
if __name__ == "__main__":  # 必须保留
    just_run()

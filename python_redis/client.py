import time

from celery import group, chain, chord

from tasks import sendmail, add, take, no_argument, xsum

# 默认一条celery队列，但是在任务执行的过程中，因为只有一条队列，所以任务执行是同步的。
result = sendmail.delay(dict(to='www.com'))
# result1 = sendmail.apply_async(args=(dict(to='windard@windard.com'), ))
# result2 = add.apply_async(args=(2, 3))

# 多条队列同步进行，需要开启多个路由, 需要在后面传入队列参数queue

result3 = take.apply_async(args=(10, 1), queue='web_tasks')
# 关联任务， 将前一个任务的结果作为参数传入下一个任务
result4 = add.apply_async(args=(2, 2), link=add.s(3), queue='default')
# # 关联任务， 将前一个任务的结果作为参数传入下一个任务
# result5 = add.apply_async(args=(2, 2), link=add.s(4), queue='default')
# # 关联任务， 将前一个任务的结果作为参数传入下一个任务
result6 = add.apply_async(args=(2, 2), link=no_argument.si(), queue='default')
# # 关联任务， 将前一个任务的结果作为参数传入下一个任务
result7 = add.apply_async(args=(2, 2), link=no_argument.signature(immutable=True), queue='default')
# 过期时间
result8 = add.apply_async(args=(2, 3), expires=10, queue='default')
# 并行调度， 结果返回列表
result9 = group(add.s(i, i) for i in range(10))(queue='default')
# 串行调度， 结果16
result10 = chain(add.s(2, 2), add.s(4), add.s(8))()
# chord - 带回调的 group
#result11 = chord((add.s(i, i) for i in range(10)), xsum.s())(queue='default')



"""
凡是任务同步执行的，比如add.delay、+add.s和串行调度都会使用Celery中默认的celery队列
而配置多个队列的异步任务则由各自的队列负责
默认队列启动：celery -A app worker  -l info
多个队列启动：celery -A app worker -Q default,web_tasks -l info
"""
# TODO

time.sleep(3)
print(result.get())
# print(result1.get())
# print(result2.get())
print(result3.get())
print(result4.get())
# print(result5.get())
print(result6.get())
print(result7.get())
print(result8.get())
print(result9.get())
print(result10.get())
#print(result11.get())






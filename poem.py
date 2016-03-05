poem = '''
这是一个喧嚣的世界
我从未感觉她安静过
她的繁荣 昌盛
给我们带来更多的疲惫和抱怨
我堵住双耳
不去听她疲惫 抱怨
也不去看她的饭桶 昌盛
我以为我的世界从此就安静了
可是
总有那么一个人
尽管她不曾对你有过一言一语
你却能听见她的声音
因为
她让你对明天有所期待
'''

import term 
import random

for line in poem.split('\n'):
    colors = [term.red,term.green,term.yellow,term.blue]
    mode = [term.bold,term.dim,term.underscore,term.blink,term.reverse]
    term.writeLine(line.strip(),random.choice(colors),random.choice(mode))

import os
import random
for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.png'):
        os.rename(file, ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(20)) + '-' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(7)) + os.path.splitext(file)[1])
    
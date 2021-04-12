#! /usr/bin/env python3

import glob
import re
import subprocess
import shlex
import asyncio
import os

async def export_one(sem, filename):
    output = re.sub(r'\.svg$', '.pdf', filename)
    cmd = [
        'inkscape',
        filename,
        '--export-area=page',
        '--batch-process',
        '--export-type=pdf',
        f'--export-filename={output}'
    ]
    async with sem:
        print(f'Converting {filename}\n', end='')
        proc = await asyncio.create_subprocess_exec(*cmd)
        await proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f'Error converting {filename}\n', end='')
        print(f'Done converting {filename}\n', end='')


async def export_all():
    sem = asyncio.Semaphore(len(os.sched_getaffinity(0)))
    tasks = (export_one(sem, name) for name in glob.glob('*/*.svg'))
    return await asyncio.gather(*tasks)

asyncio.run(export_all())

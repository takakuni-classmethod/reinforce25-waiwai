# High
def change_file_permissions_noncompliant():
    import os
    import stat
    # Noncompliant: permissions assigned to all users.
    os.chmod("sample.txt", stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

# Low

def put_object_to_queue_noncompliant(queue):
    try:
        queue.put([42, None, 'hello'])
    finally:
        queue.task_done()


def shared_queue_noncompliant():
    from multiprocessing.context import Process
    from multiprocessing.queues import Queue
    queue = Queue()
    process = Process(target=put_object_to_queue_noncompliant, args=(queue,))
    process.start()
    print(queue.get())  # prints "[42, None, 'hello']"
    # Noncompliant: uses 'Process.terminate' API on shared resources making
    # queue liable to become corrupted and may become unusable by other process
    process.terminate()
    # trying to access corrupt queue
    queue.put([50, None, 'hello'])

# Medium

def disable_gradient_calculation_noncompliant():
    import torch
    # Noncompliant: disables gradient calculation using `torch.no_grad()`.
    with torch.no_grad():
        model.eval()

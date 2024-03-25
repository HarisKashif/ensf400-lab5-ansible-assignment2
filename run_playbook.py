import shutil
from ansible_runner import run

def run_playbook():
    r = run(private_data_dir='./', playbook='hello.yml', ignore_logging=True)
    events = r.events

    for event in events:
        if 'event_data' in event:
            event_data = event['event_data']
            if 'task' in event_data:
                task = event_data['task']
                if 'status' in event_data:
                    status = event_data['status']
                    print(f'TASK [{task}] - {status.upper()}')

    # Cleanup artifacts directory after playbook run
    shutil.rmtree('./artifacts', ignore_errors=True)

if __name__ == "__main__":
    run_playbook()

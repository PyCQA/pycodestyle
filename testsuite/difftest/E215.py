#: E303
















ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jackfruit')
main_script_filename = ROOT + '/main.js'

if timeout:
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)

    args = [NODE_PATH, main_script_filename, '--template', template]

for proxy in proxies:
    args += ['--proxy', proxy]

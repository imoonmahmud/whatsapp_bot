from collections import OrderedDict

MAX_MESSAGES = 10
MAX_SEEN = 1000

_history = {}
_seen = OrderedDict()

def get_history(sender):
    return _history.get(sender, [])

def save(sender, user_text, bot_reply):
    messages = _history.setdefault(sender, [])
    messages.append({'role': 'user', 'content': user_text})
    messages.append({'role': 'assistant', 'content': bot_reply})
    _history[sender] = messages[-MAX_MESSAGES:]

def clear(sender):
    _history.pop(sender, None)

def already_processed(msg_id):
    if msg_id in _seen:
        return True
    _seen[msg_id] = True
    if len(_seen) > MAX_SEEN:
        _seen.popitem(last=False)
    return False

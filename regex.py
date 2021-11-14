# 将正则表达式翻译为 NFA

from automata import Automata

state_count = 0
buffer: list = []

def _simp_regex(): # s only contains basic characters
    global state_count
    global buffer
    state_count += 1
    start = state_count
    last_state = start
    trans = []
    while len(buffer) > 0:
        if buffer[0] != '*' and buffer[0] != '(' and buffer[0] != ')' and buffer[0] != '|':
            if len(buffer) > 1 and buffer[1] == '*':
                state_count += 1
                trans.append([last_state, state_count, ''])
                trans.append([state_count, state_count, buffer[0]])
                trans.append([state_count, state_count + 1, ''])
                state_count += 1
                last_state = state_count
                buffer.pop(0)
                buffer.pop(0)
            else: 
                state_count += 1
                trans.append([last_state, state_count, buffer[0]])
                last_state = state_count
                buffer.pop(0)
        else:
            break
    finish_states = (last_state, )
    return (start, finish_states, trans)

def _sub_regex():
    global buffer
    global state_count
    assert len(buffer) > 0 and buffer[0] == '('
    buffer.pop(0)
    start, finish_states, trans = _regex()
    assert len(buffer) > 0 and buffer[0] == ')'
    buffer.pop(0)
    if len(buffer) > 0 and buffer[0] == '*':
        buffer.pop(0)
        state_count += 1
        nstart = state_count
        state_count += 1
        nfinish = (state_count, )
        trans.append([nstart, start, ''])
        trans.append([nstart, nfinish[0], ''])
        for fstate in finish_states:
            trans.append([fstate, start, ''])
            trans.append([fstate, nfinish[0], ''])
        return (nstart, nfinish, trans)
    else:
        return (start, finish_states, trans)

def _concat_nfa(nfa1, nfa2):
    if nfa1 is None:
        return nfa2
    global state_count
    state_count += 1
    start = state_count
    state_count += 1
    finish = (state_count, )
    trans = nfa1[2] + nfa2[2]
    trans.append([start, nfa1[0], ''])
    for fstate in nfa1[1]:
        trans.append([fstate, nfa2[0], ''])
    for fstate in nfa2[1]:
        trans.append([fstate, finish[0], ''])
    return (start, finish, trans)

def _regex():
    global state_count
    global buffer
    nfa_or = []
    state_count += 1
    start = state_count
    last_nfa = None
    while len(buffer) > 0:
        if buffer[0] == '|':
            nfa_or.append(last_nfa)
            buffer.pop(0)
            last_nfa = None
        elif buffer[0] == '(':
            last_nfa = _concat_nfa(last_nfa, _sub_regex())
        elif buffer[0] == ')':
            break
        else:
            last_nfa = _concat_nfa(last_nfa, _simp_regex())
    nfa_or.append(last_nfa)
    state_count += 1
    finish = (state_count, )
    trans = []
    for nfa in nfa_or:
        trans.append([start, nfa[0], ''])
        trans.extend(nfa[2])
        for fstate in nfa[1]:
            trans.append([fstate, finish[0], ''])
    print(start, finish, trans)
    return (start, finish, trans)


def regexToAutomata(s: str):
    '''
    将正则表达式翻译为自动机
    '''
    global buffer
    global state_count
    state_count = 0
    buffer = list(s)
    start_state, finish_states, trans = _regex()
    return Automata(start=start_state, finish=finish_states, trans=trans)

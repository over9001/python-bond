import nose.plugins.skip
import bond
import pexpect

# We keep the global timeout for testing way shorter than the default of 60.
# This is done to limit execution time when tests are borken and also to spot
# performance regressions
TIMEOUT = 2


def knownfail(func):
    def wrapper():
        try:
            return func()
        except Exception as e:
            raise nose.plugins.skip.SkipTest("known failure")

    wrapper.__name__ = func.__name__
    return wrapper


def bond_repl_depth(repl):
    depth = 0
    while True:
        try:
            repl.eval('1')
        except bond.TerminatedException:
            break
        repl._proc.sendline('RETURN')
        depth += 1
    return depth

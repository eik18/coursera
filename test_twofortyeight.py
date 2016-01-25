
from twofortyeight import TwentyFortyEight
"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""

class TestSuite:
    """
    Create a suite of tests similar to unittest
    """
    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0
    
    
    def run_test(self, computed, expected, message = ""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
            self.failures += 1
    
    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg

if __name__=="__main__":
    test_this=TestSuite()
    
    #test height and width function
    ut2048=TwentyFortyEight(4,5)
    test_this.run_test(ut2048.get_grid_height(), 4, 'Grid Height does not match')
    test_this.run_test(ut2048.get_grid_width(), 5, 'Grid Width does not match')
    
    #test set/get value function
    ut2048.set_tile(3, 2, 5)
    test_this.run_test(ut2048.get_tile(3, 2),5,'Expected Value of tile does not match.')
    
    #test new_tile function - fill all but 1 tile
    ut2048=TwentyFortyEight(21,5)
    zero_counter=0
    for x in range (21*5-1):
        ut2048.new_tile()
    for row in range(21):
        for col in range(5):
            if ut2048.get_tile(row,col)==0:
                zero_counter=zero_counter+1
    test_this.run_test(zero_counter,1,"more than one zero was found")
        
    
    
    #report on tests
    test_this.report_results()

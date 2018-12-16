track = r"""
                         /--------------------------------------------------------------------------------\                                           
                 /-------+-----------------------------------\  /-------------------\                     |              /--------------------------\ 
                 |       |                                   |  |                   |                   /-+--------------+--------------\           | 
                 |       |                                   |  |                   |                   | |              |              |           | 
      /----------+-------+-----------------------------------+--+>------------------+\                /-+-+--------------+-------\      |           | 
   /--+----------+-------+-----------------------------------+\ |                   ||                | | |              |       |      |           | 
   |  |          |       |        /--------------------------++-+---------------\   ||                | | |              |       |      ^           | 
   |  |          |       |        |                          || |           /---+---++----------------+-+-+--------\     |       |      |           | 
   |  |        /-+-------+--------+--------------------------++-+\          |   |   ||                | | |        |     |       |      |           | 
   |  |        | |       |        |                          || ||          |   |   ||                | | |        |     |       |      |           | 
   |  |        | |       |        |                          || ||          |   |   ||                | | |        |     |   /---+------+---\       | 
   |  |        | |       |        |                     /----++-++----------+---+---++-------\        | | |        |     |   |   |      |   |       | 
  /+--+--------+-+-------+--------+---------------------+----++-++-----\    | /-+---++-------+--------+-+-+-------\|     |   |   |      |   |       | 
  ||  |        | |       |        |    /----------------+----++-++-----+----+-+-+---++-------+--------+-+-+---\   ||     |   |   |      |   |       | 
  ||  |/-------+-+-------+--------+\   |                | /--++-++-----+----+-+-+---++-------+-------\| | |   |   ||     |   |   |/-----+---+---\   | 
  ||  || /-----+-+-------+--------++---+----------------+-+--++-++-----+----+-+-+---++-------+\      || | |   |   ||     |   |   ||     |   |   |   | 
  ||  || |     | |       |        ||   |        /-------+-+\ || ||     |    | | |   ||       ||      || | |   |   ||     |   |   ||     |   |   |   | 
  ||  || |     | |    /--+--------++---+--------+-\     | || || ||     |    | | |   ||       ||      || | |   |   ||     |   |   ||     |   |   |   | 
  ||  || | /---+-+----+--+--------++---+--------+-+-----+-++-++-++-----+----+-+-+---++-------++------++-+-+---+--\||     |   |   ||     |   |   |   | 
  ||  || | |   | |    |  |       /++---+--------+-+-----+-++-++-++-----+----+-+-+---++--\    ||      || | |   | /+++-----+---+---++\    |   |   |   | 
  ||  || | |   | |    |  |       |||   |  /-----+-+-----+-++-++-++-----+----+-+-+---++--+----++------++-+-+---+-++++-----+---+-\ |||    |   |   |   | 
  ||  || | |   | |/---+--+-----\ |||   |  |     | |     | || || ||     |    | | |   ||  |    ||      || | |   |/++++-----+---+-+-+++--\ |   |   |   | 
  ||  || | |   | ||   |  |     | |||   |  |     | |     | || || ||     |    \-+-+---++>-+----++------++-+-+---+++++/     |   | | |||  | |   |   |   | 
  ||  || | |   | ||   |  |     | |||   |  |     | |/----+-++-++-++-----+------+-+---++--+----++------++-+-+---+++++------+\  | | |||  | |   |   |   | 
  ||  || | |   | ||   |  |     | |||   \--+-----+-++----+-++-++-++-----+------+-+---++--+----++------++-+-+---/||||      ||  | | |||  | |   |   |   | 
  ||  ||/+-+---+-++\  |  |     | ||| /----+-----+-++-\  | || || \+-----+------+-+---/|  |    ||      || | |    ||||      ||  | | |||  | |   |   |   | 
  ||  |||| |   | |||  |  |     | ||| |    |     | || |  | || ||  | /---+------+-+----+--+----++------++-+-+----++++------++--+-+-+++--+-+--\|   |   | 
  ||  |||| |   | |||  |  |     | ||| |    |     | || |  | || ||  | |   |      | |    |  |    ||      || | |    ||||      ||  | | |||  | |  ||   |   | 
  ||  |||| |   | |||  |  |     | ||| |    |     | || |  | || ||  | |   |      | |    |  |    ||      || | |    ||||      ||  | | |\+--+-+--++---/   | 
  ||  |||| |   | |||  |  |     | ||| |    |     | || |/-+-++-++--+-+---+------+-+----+--+----++------++\| |    ||||      \+--+-+-+-+--+-+--++-------/ 
 /++--++++-+---+-+++--+--+-----+-+++-+----+-----+-++-++-+-++-++--+-+---+----\ | |    |  |    ||      |||| |    |\++-------+--+-+-+-/  | |  ||         
 |||/-++++-+--\| |||  |  |     | ||| |    |     | || || | || ||  | |   |    | |/+----+--+----++----\ |||| |    | ||       |  | | |    | |  ||         
 |||| |||| |  || |||  |  |     | ||| |    |     | || || | || ||  | |   |    | |||    |  |    ||    | |||| |    | ||       |  | | | /--+-+--++---\     
 |||| |||| |  || |||  |  |     | ||| |/---+-----+-++-++-+-++-++-\| |   |    | |||    |  |    ||    | |||| |    | ||       |  | | | |  | |  ||   |     
 |||| |||| |  || |||  |  |     | ||| ||   |     | || || | || || || |   |    | |||    |  |    ||    | |||| |    | ||       |  \-+-+-+--+-+--+/   |     
 |||| |||| |  || |||  |  |     | ||| ||   |     | || || | || || || |   |    | |||    |  |    ||    | |||| |    | ||       |    | | |  | |  |    |     
 |||| |||| |  || |||  |  |     | ||| ||   |     | || ||/+-++-++-++-+---+----+-+++----+--+----++----+-++++-+----+-++-------+----+-+-+--+-+\ |    |     
 |||| |||| |  || |||  |  |     | ||| ||   |     | || |||| || || || |   | /--+-+++----+--+-\  ||    | |||\-+----+-++-------+----+-+-+--+-/| |    |     
 |||| |||| |  || |||  |  |     | ||| ||   |     | || |||| || || || |   | | /+-+++----+--+-+--++----+-+++--+----+-++-------+\   | | |  |  | |    |     
 |||| |||\-+--++-+++--+--+-----+-+++-++---+-----+-++-++++-++-++-++-+---+-+-++-+++----+--+-+--+/    | |||  |  /-+-++-------++---+-+-+--+--+-+-\  |     
 |||| ||\--+--++-++/  |  |     | ||| || /-+-----+-++-++++-++-++-++-+---+-+-++-+++----+--+-+--+-----+-+++--+--+\| ||       ||   | | |  |  | | |  |     
 |||\-++---+--/| ||   |  |     |/+++-++-+-+-----+-++-++++-++-++-++-+---+-+-++-+++----+--+\|  |     | |||  |/-+++-++-------++---+-+-+--+--+-+-+--+--\  
 |||  ||   |   | ||   |  |     ||||| || | |     | || |||| || || || |   | | || |||/---+--+++--+-----+-+++--++-+++-++-------++---+-+-+--+-\| | |  |  |  
 |||  ||   |   |/++---+--+-----+++++-++-+-+-----+-++-++++-++-++-++-+---+-+-++-++++---+--+++--+-----+-+++--++-+++-++\      ||   | | |  | || | |  |  |  
 |||  || /-+---++++---+--+-----+++++-++\| |     | || |||| || || || |   | | || ||||   |  |||  |     | |||  || ||| |||      ||   | | |  | || | |  |  |  
 |||  || | |   ||||   |  |     ||||| |||| |     \-++-++++-+/ || || |   | | || ||||   |  |||  |   /-+-+++--++-+++-+++------++---+-+-+--+-++-+-+--+\ |  
 |||  || | |   |||\---+--+-----/|||| |||| |       ||/++++-+--++-++-+---+-+-++-++++---+--+++--+---+-+-+++--++-+++-+++-\    ||   | | |  | || | |  || |  
 ||| /++-+-+---+++----+--+------++++-++++-+-------+++++++-+--++-++-+---+-+-++-++++---+--+++--+---+-+-+++--++\||| ||| |    ||   | | |  | || | |  || |  
/+++-+++-+-+---+++----+--+------++++-++++-+-------+++++++-+--++-++-+---+-+-++-++++---+--+++--+---+-+-+++\ |||||| ||| |    ||   | | |  | || | |  || |  
|||| ||| | |   |||    |  |      ||||/++++-+-------+++++++-+--++-++-+---+-+-++-++++---+--+++--+---+\| |||| |||||| ||| |    ||   | | |  | || | |  || |  
|||| ||| | |   |||    |  |      ||\++++++-+-------+++++++-+--++-++-+---+-+-++-++/|   |  |||  |   ||| |||| |||||| ||| |    ||   | | |  | || | |  || |  
|||| ||| | |   |||    |  |    /-++-++++++-+-------+++++++-+--++-++-+---+-+-++-++-+---+--+++--+---+++\|||| |||||| ||| |    ||   | | |  | || | |  || |  
|||| ||| | |  /+++----+--+-\  | || |||||| |       ||||||| |  || || | /-+-+-++-++-+---+-\|||  |   |||||||| |||||| ||| |    ||   | | |  | || | |  || |  
|||| ||| | |  ||||    |  | |  | || |||\++-+-------+++++++-+--++-/| | | | \-++-++-+---+-+++/  |   |||||||| |||||| ||| |    ||   | | |  | || | |  || |  
||||/+++-+-+--++++----+--+-+--+-++-+++-++-+-------+++++++-+--++--+-+-+-+\  || || |   | |||   |   |||||||| |||||| ||| |    ||   | | |  | || | |  || |  
|||||||\-+-+--++++----+--+-+--+-++-/|| || |      /+++++++-+--++--+-+-+-++--++-++-+---+-+++---+---++++++++-++++++-+++-+----++---+-+-+\ | || | |  || |  
|||||||  | |  |||\----+--+-+--+-++--++-++-+------++++++++-+--/|  | | | ||  || |\-+---+-+++---+---++/||||| |||||| ||| |    ||   | | || | || | |  || |  
|||||||  | |  |||/----+--+-+--+-++--++-++-+\     |||||||| |   |  | | | ||  || |  |   |/+++---+---++-+++++-++++++-+++-+----++\  | | || | || | |  || |  
|||||||  | |  ||||/---+--+-+\ | ||  || || ||     |||||||| |   |  | | | ||  || |  |   |||||   |   ||/+++++-++++++-+++-+----+++--+-+-++-+-++-+-+-\|| |  
|||||||  | |  |||||   |  | || | ||  || || ||   /-++++++++-+--\|  | | | ||  || |  |   |||||   |   |||||||| ||||||/+++-+----+++--+-+\|| | || | | ||| |  
\++++++--+-+--+++++---+--+-++-+-++--++-++-++---+-++++++++-+--++--+-+-+-++--++-+--+---+++++---+---+++++++/ |||||||||| |    |||  | |||| | || | | ||| |  
 ||\+++--+-+--+++++---+--+-++-+-++--++-++-++---+-++++++++-+--+/  | | \-++--++-+--+---++/||   |   |||||||  |||||||||| |    |||  | |||| | || | | ||| |  
 || |||  |/+--+++++---+--+-++-+-++--++-++-++---+-++++++++-+--+-\ | |   ||  || |  |   || ||   |   |||||||  |||||||||| |    |||  | |||| | || | | ||| |  
/++-+++--+++--+++++---+--+-++-+-++--++-++-++---+-++++++++-+--+-+-+-+---++--++\|  |   || ||   |   |||||||  |||||||||| |    |||  | |||| | ^| | | ||| |  
||| |||  |||  ||\++---+--+-++-+-++--++-++-++---+-++++++++-+--+-+-+-+---++--++++--+---++-++---+---+++++++--+++++++++/ |    |||  | |||| | || | | ||| |  
||| |||  |||  || ||   |  | || | ||  || || ||   | |||||||| |  | | | |   ||  ||||  |   || ||   |   |||||||  |||||||||  |    |||  | |||| | || | | ||| |  
|||/+++--+++--++-++---+--+-++\| ||  || || ||   | |||||||| \--+-+-+-+---++--++++--+---++-++---+---++++/||  |||||||||  |  /-+++--+-++++-+-++\| | ||| |  
|||||||  |||  || ||   \--+-++++-++--++-++-++---+-+/||||||    | | | |   ||  ||||  |   || ||   |   ||\+-++--+++++++++--+--+-+++--+-++++-+-++++-+-/|| |  
|||^|||  |||  || ||      |/++++-++--++-++-++---+-+-++++++----+-+-+-+---++--++++--+---++-++---+---++-+-++--+++++++++--+--+-+++\ | |||| | |||| |  || |  
|||||||  |||  || ||      |||||| ||  || || ||   | | ||||||    | | | |   ||  ||||  |   |\-++---+---++-+-++--+++++++++--+--+-++/| | ||\+-+-++++-+--/| |  
|||||||  |||  ||/++------++++++-++--++-++-++---+-+-++++++-\  | | | |   ||  ||||  |   |  ||   |   || | ||  |||||||||  |  | || | | || | | |||| |   | |  
|||||||  |||/-+++++------++++++\|| /++-++-++---+-+\|||||| |  | | | |   ||  ||||  |   |  ||   |   || | ||  |||||||||  |  | || | | || | | |||| |   | |  
|||||||  |||| |||||      \++++++++-+++-++-++---+-++++++++-+--+-+-+-+---++--++++--+---+--++---+---++-+-++--/||||||||  |  | || | | || | | |||| |   | |  
|||||||  |||| v||||     /-++++++++-+++-++-++---+-++++++++-+--+-+-+-+---++--++++--+\  |  ||   |   || | ||   ||||||||  | /+-++-+-+-++-+\| |||| |   | |  
|||||||  |||| |||||     | ||v||||| ||| ||/++->-+-++++++++-+--+-+-+-+---++--++++--++--+--++---+---++-+-++-\ ||||||||  | || || | | || ||| |||| |   | |  
|||||||  |||| ||||| /---+-++++++++-+++-+++++--\| |||||||| |  | |/+-+---++--++++--++--+--++---+---++-+-++-+-++++++++--+-++-++-+-+-++-+++\|||| |   | |  
|||||||  |||| ||||| |   | |||||||| ||| |||||  || |||||||| |  | ||| |   || /++++--++--+--++---+---++\| || | |||||^||  | || || | | || |||||||| |   | |  
|||||||  |||| ||||| |   | |||||||| ||| |||||  || ||\+++++-+--+-+++-+---++-+++++--++--+--++---+---++++-++-+-++++++++--+-++-/| | | || |||||||| |   | |  
|||||||  |||| ||||| |   | |||||||| ||| |||||  || || \++++-+--+-+++-+---++-+++++--++--+--++---+---++++-++-+-++++++++--/ ||  | | | || |||||||| |   | |  
|||||||  |||| ||||| |   | |||||||| ||| |||||  || \+--++++-+--+-+++-+---++-+++++--++--+--++---+---++++-++-+-++++++++----++--+-+-+-++-/||||||| |   | |  
|||||||  |||| ||||| |   | |||||||| ||| |||||  ||  |  |||| |  | ||| |  /++-+++++--++--+--++---+---++++-++\| ||||||||    ||  | | | ||  ||||||| |   | |  
^||||||  |||| ||||| |   | |||||||| \++-+++++--++--/  |||| |  | ||| |  ||| |||||  ||  |  ||   |   |||| |||| ||||||||    ||  | | | ||  ||||||| |   | |  
|||||||  |||| ||\++-+---+-++++++++--++-+++++--++-----++++-/  | ||| |  ||| |||||  ||  |  ||   |   |||| |||| ||||||||    ||  | | | ||  ||||||| |   | |  
|||||||  |||| || || |   | ||||||||  || ||||| /++-----++++----+-+++-+\ ||| |||||  ||  |  ||   |   |||| |||| ||||||||    ||  | | | ||  ||||||| |   | |  
|||||||  |||| || || |   | ||||||||  || ||||| |||     ||||    | ||| || ||| |||||  ||  |  ||   |   |||| \+++-++++++++----++--+-+-+-/|  ||||||| |   | |  
|||||||  |||| || || |   \-++++++++--++-+++++-+++-----++++----+-+++-++-+++-+++++--+/  |  ||   |   ||||  ||| ||||||||    ||  |/+-+--+--+++++++-+\  | |  
|||||||  |||| || || |     ||||||||  || ||||| |||     ||||    | ||| || ||| |||||  |   |  ||   |   ||||  ||| ||\+++++----++--+++-+--+--+++++++-/|  | |  
|||||||  |||| || || |     ||||||||  |\-+++++-+++-----/|||    | ||| || ||| ||||| /+---+--++---+---++++--+++-++-+++++----++--+++-+\ |  |||||||  |  | |  
|||||||  |||| || || |     ||||||||  |  ||||| |||      |||    | |\+-++-+++-+++++-++---+--++---+---++++--+++-++-+++++----++--+++-++-+--++/||||  |  | |  
|||||||  |||| || || |     ||||||||  \--+++++-+++------+++----+-+-+-++-+++-+++++-++---+-<++---+---+/||  ||| || |||||    ||  ||| || |  || ||||  |  | |  
|||||||  |||| || ||/+-----++++++++-----+++++-+++------+++----+-+-+-++-+++-+++++-++---+--++\  |   | ||  ||| || |||||    ||  ||| || |  || ||||  |  | |  
|\+++++--++++-++-++++-----++++++++-----+++++-+++------+++----+-+-+-++-+++-++/|| ||   |/-+++--+---+-++--+++-++-+++++----++--+++-++-+--++-++++--+\ | |  
\-+++++--++++-++-++++-----++++++++-----+++++-+++------+++----+-+-+-++-+++-++-/\-++---++-+++--+---+-++--+++-++-++++/    ||  ||| || |  || ||||  || | |  
  |||||  |||| || ||||     ||||\+++-----+++++-+++------+++----+-+-+-++-+++-++----++---++-+++--+---+-+/  ||| || ||||     |\--+++-++-+--++-++/|  || | |  
  |||||  |||| || ||||    /++++-+++-----+++++-+++------+++----+-+-+-++-+++-++----++---++-+++-\|   | |   ||| || ||||     |   ||| || |  || || |  || | |  
  |||||  |||| || ||||/---+++++-+++-----+++++-+++-----<+++----+-+-+-++-+++-++----++---++-+++-++---+-+---+++-++-++++---\ |   ||| || |  || || |  || | |  
  |||||  |||| || |||||   ||||| |||     ||||| |||      |||    | | | || ||| ||/---++---++-+++-++---+-+---+++-++-++++---+-+---+++-++-+--++-++-+-\|| | |  
  |||||  |||| || |||||   ||||| |||   /-+++++-+++------+++----+-+-+-++-+++-+++---++---++-+++-++---+-+---+++-++-++++---+-+---+++-++\|  || || | ||| | |  
  ||||\--++++-++-+++++---+++++-+++---+-+++++-+++------+++----+-+-+-++-+++-+++---++---/| ||| || /-+-+---+++\|| ||||   | |   ||| ||||  || || | ||| | |  
  ||||   |||| |\-+++++---+++++-+++---+-+++++-+++------+++----+-+-/ || ||| ^||   ||    | ||| || | | |   |||||| ||||   | |   ||| ||||  || || | ||| | |  
  ||||   |||| |  |||||/--+++++-+++---+-+++++-+++------+++----+-+---++-+++-+++---++----+-+++-++-+\| |   |||||| ||||   | |   ||| ||||  || || | ||| | |  
  ||||   |||| |  ||||||  ||||| |||   | ||||| |||      |||    | |   || |||/+++---++---\| ||| || ||\-+---++++++-++++---+-+---+++-++++--++-++-+-+++-/ |  
  ||||   |||| |  ||||||  ||||| |||   | ||||| |||      |||    | |   || |||||||   ||   || ||| || ||  |   |||||| ||||   | |   ||| ||||  || || | |||   |  
  ||||   |||| |  ||||||  ||||| |||   | ||||| |||      |||    | |   || |||||||   || /-++-+++-++-++--+---++++++-++++\  | \---+++-++++--/| || | |||   |  
  \+++---++++-+--++++++--+++++-+++---+-+++++-+++------+++----+-+---++-+/|||||   || | || ||| || ||  |   |||||| |||||  |     ||| ||||   | || | |||   |  
   \++---++++-+--++++++--++++/ |||   | ||||| |||      \++----+-+---++-+-+++++---++-+-++-+++-++-++--+---/||||| |||||  |     ||| ||||   | || | |||   |  
    ||   |||| |  ||||||  ||||  ||\---+-+++++-+++-------++----+-+---++-+-+++++---++-+-++-/|| || ||  |    ||||| |\+++--+-----+++-++++---/ || | |||   |  
    ||   |||| |  ||||||  |\++--++----+-+++++-+++-------++----+-+---++-+-+++++---++-+-++--++-++-++--+----+++++-+-+++--+-----++/ ||||     || | |||   |  
    ||   |||| |  |\++++--+-+/  ||    | ||||| |||       ||    | |   || \-+++++---++-+-++--++-++-++--+----/|||| | |||  |     ||  ||||     || | |||   |  
    ||   |||| |  | ||||  | |   ||    |/+++++-+++----\  ||    | |   ||   |||||   || | ||  || || ||  |     |||| | |||  |     ||  ||||     || | |||   |  
    ||   |||| |  | ||||  | |   ||    |||\+++-+++----+--++----+-+---++---+++++---++-+-++--++-++-++--+-----++++-/ |||  |     ||  ||||     || | |||   |  
    ||   |||| |  | ||||  | |   ||    \++-+++-+++----+--++----+-+---++---+++++---++-+-++--++-++-++--+-----++++---+++--+-----++--++/|     || | |||   |  
    ||   |||| |  | ||||  | |   ||     || ||| ||\----+--++----/ |   ||   |||||   || | ||  || || ||  |     ||||   |||  |     ||  || |     || | |||   |  
    ||   |||| |  | ||||  | |   ||     || ||| ||     |  |\------+---++---+++++---++-+-++--++-+/ ||  |     ||||   ||| /+-----++--++-+\    || | |||   |  
    ||   ||\+-+--+-++++--+-+---++-----++-+++-++-----+--+-------+---++---+++++---++-+-++--++-+--++--+-----++++---+/| ||     ||  || ||    || | |||   |  
    ||   || | |  | ||||  | |   ||     || ||| ||  /--+--+-------+---++---+++++---++-+-++--++-+--++--+-<---++++--\\-+-++-----++--++-/|    || | |||   |  
 /--++---++-+-+--+-++++--+-+---++----\|| ||| ||  |  |  |       |   ||   |||||   || | ||  || |  ||  |     ||||  |  | ||     ||  ||  |    || | |||   |  
 |  ||   || | |  | ||||  | |   ||    ||| |\+-++--+--+--+-------+---++---+++++---++-+-++--++-+--++--+-----++++--+--+-++-----++--/|  |    || | |||   |  
 |  ||   || | |  | ||||  | |   ||    ||| | | ||  |  |  |       |   ||   |\+++---++-+-/\--++-+--++--+-----++++--+--+-++-----++---+--+----++-+-++/   |  
 |  ||   \+-+-+--+-++++--+-+---++----++/ | | ||  |  |  |       |   ||   | |||   || |     || |  ||  |     ||||  |  | ||     ||   |  |    || | ||    |  
 |  ||    | | |  | ||||  | |   ||    ||/-+-+-++-\|  |  |       |   ||  /+-+++---++-+-----++-+--++--+-----++++--+--+-++\    |\---+--+----++-+-+/    |  
 |  ||    | | |  | ||||  | |   ||    ||| | | || ||  |  | /-----+---++-\|| |||   || |     || |  ||  ^     ||||  |  | |||    |    |  |    || | |     |  
 |  ||    | \-+--+-++++--+-+---/|    ||| | | || ||  |  | |     |   || ||| |||   |\-+-----++-+--++--+-----++++--+--+-+++----+----+--+----/| | |     |  
 |  ||    |   |  | ||||  | |    |    ||| \-+-++-++--+--+-+-----+---++-+++-+++---+--+-----++-+--++--+-----/|||  |  | |||    |    |  |     | | |     |  
 |  ||    |   |  \-++++--+-+----+----+++---/ || ||  |  | |     |   || ||| |||   |  |     || |  ||  |      ||| /+--+-+++--\ |    |  |     | | |     |  
 |  ||    |   |    ||||  | |    |    |||     \+-++--+--+-+-----+---+/ ||| |||   |  |     || |  ||  |      ||| ||  | |||  | |    |  |     | | |     |  
 |  ||    |   \----++++--+-/    |    |||      | ||  |  | |     |   \--+++-+++---+--+-----++-+--++--+------+++-++--+-+++--+-+----+--+-----+-/ |     |  
 |  ||    |        ||||  |      \----+++------+-++--+--+-+-----+------+++-+++---+--+-----/| |  \+--+------/|| ||  | |||  | |    |  |     |   |     |  
 |  |\----+--------++++--+-----------+++-<----+-++--+--+-+-----+------+++-+++---+--+------+-+---+--+-------+/ ||  | |||  | |    |  |     |   |     |  
 |  |     |        |\++--+-----------+++------/ |\--+--+-+-----+------+++-+++---+--+------+-+---+--+-------+--+/  | |||  | |    |  |     |   |     |  
 |  |     |        | ||  |           |||        |   |  | |     |      ||| |\+---+--+--<---+-+---+--+-------+--+---+-+++--+-/    |  |     |   |     |  
 |  |     |        | ||  |           |||        |   |  | |     |      ||| | \---+--+------+-+---+--+-------+--+---+-+++--+------+--+-----+---/     |  
 |  |     |        | ||  |           ||\--------/   |  | \-----+------/|| |     |  |      | |   |  |       |  |   | |||  |      |  |     |         |  
 |  |     |        | ||  |           ||             |  |       |       || |     |  \------+-+---+--+-------+--+---/ \++--+------+--/     |         |  
 |  |     |        | ||  \-----------++-------------+--+-------+-------++-+-----+---------+-/   |  |       |  |      ||  |      |        |         |  
 |  |     |        | |\--------------++-------------+--+-------+-------++-+-----+---------+-----/  |       |  |      ||  |      |        |         |  
 |  \-----+--------+-+---------------++-------------+--+-------+-------+/ |     |         |        |       |  \------++--/      |        |         |  
 |        |        | |               ||             |  |       |       \--+-----+---------+--------+-------+---------+/         |        |         |  
 |        |        | |               ||             |  |       |          |     |         |        |       |         |          |        |         |  
 |        |        | |               ||             |  |       |          |     |       /-+--------+-------+---------+----------+--------+--\      |  
 \--------+--------+-+---------------/|             |  |       |          |     |       | |        |       |         |          |        |  |      |  
          \--------+-+----------------+-------------+--+-------/          |     |       | |        |       |         |          |        |  |      |  
                   | |                |             |  \------------------+-----+-------+-+--------+-------+---------+----------+--------/  |      |  
                   | \----------------+-------------+---------------------+-----+-------+-+--------+-------+---------/          |           |      |  
                   \------------------+-------------+---------------------+-----+-------+-/        |       |                    |           |      |  
                                      |             |                     |     |       |          |       \--------------------+-----------+------/  
                                      |             |                     |     \-------+----------+----------------------------/           |         
                                      |             |                     \-------------+----------/                                        |         
                                      \-------------/                                   |                                                   |         
                                                                                        \---------------------------------------------------/         
"""
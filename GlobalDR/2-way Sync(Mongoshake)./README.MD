Mongoshake를 사용하면서 양방향 실시간 동기화를 하는 과정에 대한 기록입니다.

단방향 동기화는 쉽지만 양방향 동기화를 하기 위해서는 DB에 존재하는 Checkpoint DB를 동기화에서 제외해 주어야합니다. 


mongoshake 프로그램에서 제공하는 Comparsion 파일이 존재하는데 기능이 특정 DB나 특정 Collection을 제외하는 기능만 존재하고 있는데

실제 현업에서는 exclude 기능 만큼 include 기능이 필요할 것이라고 생각하여 해당 기능을 Script를 수정하면서 추가하였습니다.

--includeDB --includeCollection 기능 추가

# Github Intructions
### 1. Git hub 연결 
- git clone 주소

### 2. 폴더, 파일 올리기
- main / develop 어디에 올리지 정하기
- 현재 나의 위치 파악하여 올리려는 파일의 폴더에 맞추기 cd 폴더 이름
- git add ./파일 이름
- git commit –m "설명"
- git push

##### * 같은 파일인데 수정사항 있다고 하면 저장하고 2번과 같은 방법으로 진행한다면 덮어씌어짐

### 3. 다른 팀원이 올린 파일 가져오기
- main/develop 정하기
- git pull

### 4. github에 올라와 있는 파일 삭제하기 (남이 올린 것도 본인이 삭제 가능)
- 내 컴퓨터로 가져오지 않는 경우라면, 먼저 pull 해오기
- 그 다음 vscode 내에서 삭제
- git add ./삭제할 파일 이름
- git commit –m “DEL”
- git push 

### 5. 기타
- 브랜치 생성 git checkout –b 만들고자 하는 브랜치이름
- 브랜치 이동 git checkout 브랜치이름

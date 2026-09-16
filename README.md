# India

## Activity 1: Create repo & first commit (Proof of Commit)
<img width="1436" height="546" alt="Screenshot 2026-09-16 at 2 15 39 PM" src="https://github.com/user-attachments/assets/45df6416-dff2-47e0-99db-60851e7dcbca" />

## Activity 2: Branching and merging (Output of the Merge Command)
<img width="1430" height="811" alt="Screenshot 2026-09-16 at 2 22 06 PM" src="https://github.com/user-attachments/assets/05a50a2f-a8df-411d-82bc-495b5d5851e1" />

## Activity 3: Issues, PRs, and merge conflicts (Successful Merge)
<img width="765" height="476" alt="Screenshot 2026-09-16 at 2 56 39 PM" src="https://github.com/user-attachments/assets/9988ca7f-c683-4125-b258-6cb32580f6fb" />

## Activity 4: Unit tests (Result of Commit)
<img width="697" height="201" alt="Screenshot 2026-09-16 at 4 32 11 PM" src="https://github.com/user-attachments/assets/472349ce-7bd3-487f-b57d-6427b81e2c4a" />
<img width="1427" height="747" alt="Screenshot 2026-09-16 at 4 31 52 PM" src="https://github.com/user-attachments/assets/61325050-d7d1-45a2-8849-98c28bb027e6" />

## Activity 5: Git rebase (Outputs from Process)
**_note:_** C4 is accidentally also labelled C3. the two C3's can be told apart because the **correct C3** is associated with file1 while the **incorrect C3 (actually C4)** is associated with file2.

**Photo 1:** order before rebasing

<img width="865" height="387" alt="Screenshot 2026-09-16 at 4 41 54 PM" src="https://github.com/user-attachments/assets/7b9cda71-7201-40c1-88fc-b1fd671e9acf" />

* command: git log --oneline --graph --all
* shows the divergence before rebasing
* can see the rebase branch (with commits c1 and c2) forked off an older point in history, while develop moved ahead separately with two new commits
* the two branches have separate histories at this point

**Photo 2:** order after rebasing

<img width="797" height="234" alt="Screenshot 2026-09-16 at 4 42 33 PM" src="https://github.com/user-attachments/assets/7da2d090-cdb2-4642-920c-cea23fdc1327" />

* git log --oneline on the rebase branch after running git rebase develop
* shows the final linear order with the newest at top: c2, then c1, then develop's two commits below them.
* new order: C2 -> C1 -> C4 (incorrectly labelled C3) -> C3

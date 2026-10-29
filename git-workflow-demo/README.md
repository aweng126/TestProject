# GitHub 分支与 PR 练习

这个目录用一个仅依赖 Python 3 标准库的小程序，演示从修改代码到合并 PR 的完整流程。
以下命令均在 `TestProject` 仓库根目录执行；本仓库的默认分支为 `master`。

## 运行示例

```bash
python3 git-workflow-demo/hello.py
# 你好，GitHub！

python3 git-workflow-demo/hello.py --name Ghostty
# 你好，Ghostty！

python3 git-workflow-demo/hello.py --help
```

## 1. 获取项目并确认提交身份

首次使用时克隆仓库；已有本地副本时，直接进入对应目录即可。

```bash
gh repo clone aweng126/TestProject
cd TestProject
git remote -v
git config --get user.name
git config --get user.email
```

提交姓名、邮箱是 commit 的署名；`gh auth status` 检查的是访问 GitHub 的登录身份。
两者分别配置。

## 2. 从最新默认分支创建工作分支

先确认 `git status` 没有尚未处理的本地修改，再切换分支。

```bash
git switch master
git pull --ff-only
git switch -c learn/first-pr-workflow
```

工作分支用于保存本次修改，`master` 暂时保持原样。
如果同名分支已存在，请为下一次练习选择不同的分支名。

## 3. 修改代码并在本地检查

例如，用编辑器修改 `hello.py` 的默认问候名字，然后运行程序确认结果。

```bash
python3 git-workflow-demo/hello.py
python3 git-workflow-demo/hello.py --name Ghostty
git status
git diff
git diff --check
```

`git diff` 显示已有文件的未暂存修改；新增文件可以直接用编辑器查看，或暂存后通过
`git diff --cached` 检查。

## 4. 暂存并提交

```bash
git add README.md git-workflow-demo/README.md git-workflow-demo/hello.py
git diff --cached
git commit -m "feat: add GitHub PR workflow demo"
```

`git add` 选择本次提交的内容；`git commit` 将内容记录到本地分支。

## 5. 推送远程分支

```bash
git push -u origin HEAD
```

这一步把当前分支上传到 `origin`，并建立本地分支与远程分支的跟踪关系。
之后在同一分支继续修改、提交时，运行 `git push` 即可更新远程分支和已有 PR。

## 6. 创建并检查 PR

```bash
gh pr create --base master
gh pr diff
gh pr checks
```

按提示填写标题和说明。PR 提议将工作分支合并到 `master`。
如果仓库没有配置自动检查，`gh pr checks` 会提示没有检查；此时仍需完成本地验证。

## 7. 合并并同步本地默认分支

检查修改、确认需要的测试通过后：

```bash
gh pr merge --squash --delete-branch
git switch master
git pull --ff-only
git status
git log --oneline -5
```

`--squash` 将 PR 内的修改合并为默认分支上的一个提交；
`--delete-branch` 清理已经合并的工作分支。
合并后，后续任务应从最新的 `master` 创建新分支。

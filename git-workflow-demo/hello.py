"""A small command-line program for practicing the GitHub PR workflow."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="输出一句问候，练习修改、提交和 PR 流程。")
    parser.add_argument("--name", default="GitHub!", help="问候的名字，默认为 GitHub")
    args = parser.parse_args()
    print(f"你好，{args.name}！")


if __name__ == "__main__":
    main()

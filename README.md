# Python 项目自动打包说明

## 概述
本仓库实现了一个自动化的 Python 项目打包流程，通过 GitHub Actions，每当向 `main` 分支（可根据实际配置修改触发分支）推送代码时，会自动检测 `script` 文件夹下各个项目是否已经打包。如果未打包，则按照对应项目文件夹内 `set.json` 配置文件指定的设置进行打包，并将打包后的文件提交回仓库的 `dist` 文件夹中。

## 项目结构说明
- `.github/workflows/build_python_projects.yml`：GitHub Actions 工作流配置文件，定义了整个自动化打包的流程逻辑，包括环境设置、项目遍历、依赖安装、打包操作以及提交更改等步骤。
- `script`：存放各个 Python 项目的文件夹，每个项目子文件夹下需要包含一个 `main.py`（或项目主 Python 脚本文件）以及对应的 `set.json` 配置文件。
- `set.json`：用于配置项目打包相关的重要信息，具体配置项如下：
  - `packaging_platform`：指定打包平台，目前支持 `pyinstaller` （可根据需要扩展其他打包方式）。
  - `python_version`：项目期望运行的 Python 版本，工作流会根据此配置来设置相应的 Python 环境。
  - `python_dependencies`：列出项目运行所依赖的 Python 库，在打包前会通过 `pip` 进行安装。
  - `special_parameters`：针对不同打包平台的特殊参数设置。例如对于 `pyinstaller`，可以设置诸如：
    - `onefile`：是否生成单文件可执行文件
    - `name`：可执行文件名称
    - `add_data`：要添加的数据文件或文件夹
    - `hidden_imports`：隐藏导入的模块
- `dist`：用于存放打包好的项目文件，最终打包后的 `.tar.gz` 文件会存放在此文件夹中，并且通过工作流自动提交回仓库。

## 使用步骤

### 1. 准备项目
在 `script` 文件夹下创建你的 Python 项目文件夹，例如 `project1`、`project2` 等。在每个项目文件夹内放入你的 Python 脚本文件（如 `main.py`），以及按照上述格式编写好的 `set.json` 配置文件，确保配置文件中的各项参数符合项目需求。

### 2. 推送代码
将准备好的项目相关文件添加、提交并推送到仓库的相应分支（默认是 `main` 分支，若工作流配置中修改了触发分支，则推送到对应的分支）。推送操作会触发 `.github/workflows/build_python_projects.yml` 中定义的 GitHub Actions 工作流，自动执行打包流程。

### 3. 查看打包结果
在工作流执行完成后，可以在仓库的 `dist` 文件夹中查看打包好的项目文件（.tar.gz 格式）。

## 注意事项
- 确保 `set.json` 文件中的配置信息准确无误，特别是 `python_dependencies` 以及 `pyinstaller`（如果使用该打包平台）的各项特殊参数，错误的配置可能导致打包失败或者生成的可执行文件无法正常运行。
- 如果在打包过程中出现问题，可以查看 GitHub Actions 的执行日志，它会详细记录每一步的操作及可能出现的错误信息，便于排查问题并进行相应的调整。

请注意，在上述 GitHub Actions 脚本中，`git config` 那两步需要将 `"Your GitHub Username"` 和 `"your_email@example.com"` 替换为你自己的真实 GitHub 用户名和邮箱地址，这样才能正确地进行提交操作。另外，自动提交操作可能需要配置相应的权限（比如通过创建 GitHub 仓库的 PAT - 个人访问令牌，并配置到仓库的 Secrets 中，在工作流中使用该令牌来进行提交等，此处为简化示例未详细体现这部分配置过程），具体配置方式可参考 GitHub 官方文档相关内容。

希望这个完整的示例能满足你的需求，你可以根据实际项目情况进一步调整和完善各个部分的内容。

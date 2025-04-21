#!/usr/bin/env python3
"""
依赖检查脚本，用于验证项目所需的依赖是否正确安装。
"""


try:
    import importlib
    import sys
    import pkg_resources  # 动态导入以避免直接失败
except ImportError as e:
    print(f"错误：缺少必要模块 {e.name}。请运行以下命令安装：")
    print("pip install setuptools")
    sys.exit(1)

from pkg_resources import DistributionNotFound, VersionConflict

def check_module(module_name):
    """检查模块是否可以导入。"""
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def check_version(requirement):
    """检查包是否满足版本要求。"""
    try:
        pkg_resources.require(requirement)
        return True
    except (DistributionNotFound, VersionConflict):
        return False


def main():
    """主函数，用于检查依赖。"""
    print("正在检查依赖...\n")
    
    # 核心模块检查
    modules = {
        "bs4": "BeautifulSoup",
        "openai": "OpenAI API",
        "pandas": "数据处理",
        "pymysql": "MySQL 连接",
        "lxml": "XML/HTML 解析",
        "openpyxl": "Excel 支持",
        "xlrd": "Excel 支持（旧文件）",
        "jsonpath": "JSON 解析",
        "requests": "HTTP 请求"
    }
    
    # 检查模块是否可以导入
    missing_modules = []
    for module, description in modules.items():
        if check_module(module):
            print(f"✓ {module} - {description}")
        else:
            missing_modules.append(module)
            print(f"✗ {module} - {description} (缺失)")
    
    print("\n正在检查版本要求...\n")
    
    # 从文件中读取依赖
    try:
        with open("requirements.txt", "r") as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print("✗ requirements.txt 文件未找到！")
        requirements = []
    
    # 检查版本要求
    version_issues = []
    for req in requirements:
        if req and not req.startswith("#"):
            if check_version(req):
                package = req.split("==")[0] if "==" in req else req
                print(f"✓ {package} 满足版本要求")
            else:
                version_issues.append(req)
                package = req.split("==")[0] if "==" in req else req
                print(f"✗ {package} 版本问题")
    
    # 总结
    print("\n依赖检查总结：")
    if not missing_modules and not version_issues:
        print("所有依赖已正确安装！")
    else:
        if missing_modules:
            print(f"缺失模块：{', '.join(missing_modules)}")
        if version_issues:
            print(f"版本问题：{', '.join(version_issues)}")
        print("\n要修复这些问题，请运行：")
        print("pip install -r requirements.txt")


if __name__ == "__main__":
    main()
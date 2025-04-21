```bash
pip install bs4
pip install jsonpath
pip install lxml 
 

pip install requests
```

## 设置环境

```bash
# 使用 venv 模块来创建虚拟环境并放到.venv 目录下
python -m venv .venv

# 激活虚拟环境，使当前 shell 会话使用该虚拟环境中的 Python 解释器和包。
.venv/Scripts/activate
# 退出虚拟环境
deactivate 

# 读取 requirements.txt 文件中的内容，并根据其中列出的包名和版本号自动安装所有依赖。
pip install -r requirements.txt

# 删除虚拟环境
rm -r .venv/
```

```bash
# 生成一个包含当前环境所有依赖的 requirements.txt 文件。
pip freeze > requirements.txt
# 卸载requirements的依赖
pip uninstall -r requirements.txt 

```

### 添加新依赖

1. 在您的虚拟环境中安装包：
   ```
   pip install package_name
   ```

2. 将其添加到 requirements.txt：
   ```
   pip freeze > requirements.txt
   ```
   
   或者手动将其添加到 requirements.txt 并指定版本：
   ```
   package_name==1.0.0
   ```

### 更新依赖

1. 在虚拟环境中更新包：
   ```
   pip install --upgrade package_name
   ```

2. 更新 requirements.txt：
   ```
   pip freeze > requirements.txt
   ```

### 最佳实践

1. 始终使用虚拟环境进行隔离
2. 保持 requirements.txt 更新
3. 为所有依赖指定版本号
4. 在 requirements.txt 中按类别分组依赖
5. 使用 pip-tools 或 Poetry 进行更高级的依赖管理

## 退出环境

```
deactivate
```
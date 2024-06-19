from setuptools import setup, find_packages

setup(
    name='ft_fastapi',  # 包名
    version='0.1.0',  # 版本号
    author='ZhuangLiu',  # 作者名
    author_email='assignment406@126.com',  # 作者邮箱
    description='A simple FastAPI application',  # 简短描述
    long_description=open('README.md').read(),  # 长描述，通常是README文件的内容
    long_description_content_type='text/markdown',  # 长描述的格式
    url='https://github.com/dufe-fintech/ft_fastapi',  # 项目主页
    packages=find_packages(),  # 自动查找项目中的所有包
    install_requires=[
        'fastapi>=0.63.0',  # 项目依赖，根据实际情况填写
        'uvicorn[standard]',  # 用于运行FastAPI应用的ASGI服务器
        # 其他依赖
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # 开发状态
        'Intended Audience :: Developers',  # 目标用户
        'Topic :: Software Development :: Libraries :: Application Frameworks',  # 主题
        'License :: OSI Approved :: MIT License',  # 许可证
        'Programming Language :: Python :: 3',  # 支持的Python版本
        'Programming Language :: Python :: 3.8',  # 具体Python版本
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',  # 支持的Python版本范围
    include_package_data=True,  # 包含包数据
    zip_safe=False
)

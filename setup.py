from setuptools import setup, find_packages

setup(
    name='ft_fastapi',
    version='0.1.0',
    author='ZhuangLiu',  # 作者名
    author_email='assignment406@126.com',  # 作者邮箱
    description='A simple FastAPI application',  # 简短描述
    # long_description=open('README.md').read(),  # 注释掉或删除这行
    long_description_content_type='text/plain',  # 如果你注释掉了 long_description，这行也可以删除
    url='https://github.com/dufe-fintech/ft_fastapi',
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.63.0',
        'uvicorn[standard]',
        # 其他依赖项
    ],
    classifiers=[
        # 项目分类器
    ],
    python_requires='>=3.8',
    include_package_data=True,
    zip_safe=False
)

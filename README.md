# hello-rpm

## rpmbuild 命令主要参数

`rpmbuild` 是用于构建 RPM 包的核心命令。以下是其主要参数说明：

### 构建阶段参数

- **`-bp`** - 执行 %prep 阶段（解压源代码）
- **`-bc`** - 执行到 %build 阶段（编译）
- **`-bi`** - 执行到 %install 阶段（安装到 buildroot）
- **`-bb`** - 构建二进制 RPM 包
- **`-bs`** - 构建源码 RPM 包（SRPM）
- **`-ba`** - 构建二进制和源码 RPM 包

### 常用选项

- **`--define "macro value"`** - 定义宏变量
  - 示例: `rpmbuild --define "_topdir /path/to/rpmbuild" -ba example.spec`
- **`--clean`** - 构建完成后清理 BUILD 目录
- **`--nodeps`** - 不检查依赖关系
- **`--target <arch>`** - 指定目标架构
  - 示例: `rpmbuild --target x86_64 -ba example.spec`
- **`--rebuild`** - 从 SRPM 重新构建
- **`--recompile`** - 从 SRPM 编译并安装

### 目录结构相关

默认 rpmbuild 使用以下目录结构：
- `BUILD/` - 构建过程中的临时文件
- `RPMS/` - 生成的二进制 RPM 包
- `SOURCES/` - 源代码和补丁文件
- `SPECS/` - RPM spec 文件
- `SRPMS/` - 生成的源码 RPM 包

### 使用示例

```bash
# 构建二进制 RPM 包
rpmbuild -bb hello-rpm.spec

# 构建源码和二进制 RPM 包
rpmbuild -ba hello-rpm.spec

# 使用自定义 topdir
rpmbuild --define "_topdir $HOME/rpmbuild" -ba hello-rpm.spec

# 只执行准备阶段（调试用）
rpmbuild -bp hello-rpm.spec
```
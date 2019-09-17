from django import forms
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response

from .models import Snippet,LeetCode
from .serializers import SnippetSerializer

from django.views.generic import ListView,DetailView

class LeetCodeList(ListView):
	model = LeetCode
	context_object_name = 'leetcodes'
	# template_name = 'card/leetcode_list.html'


class LeetCodeDetail(DetailView):
	model = LeetCode
	context_object_name = 'leetcode'
	# template_name = 'card/leetcode_detail.html'


class SnippetForm(forms.ModelForm):
	class Meta:
		model = Snippet
		fields = ['question', 'code','output','reason']

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	renderer_classes = [JSONRenderer]

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	renderer_classes = [JSONRenderer,TemplateHTMLRenderer]

	def get(self,request,*args,**kwargs):
		self.object = self.get_object()
		print(request.accepted_renderer.format)
		print(request.accepted_media_type)

		if request.accepted_renderer.format == 'html':
			return render(request,'card/snippet_detail.html',{'snippet':self.object})
		else:
			serializer = SnippetSerializer(instance=self.object)
			data = serializer.data
			# content 返回的是json字符串,ajax 还要解析
			# data 返回的是 json 对象,ajax 直接取属性
			# content = JSONRenderer().render(serializer.data)
			return Response(data)

		

BUILTINS = {'string': '常见的字符串操作', 're': '正则表达式操作', 'difflib': '计算差异的辅助工具', 'textwrap': '文本自动换行与填充', 'unicodedata': 'Unicode 数据库', 'stringprep': '因特网字符串预备', 'readline': 'GNU readline 接口', 'rlcompleter': 'GNU readline 的补全函数', 'struct': '将字节串解读为打包的二进制数据', 'codecs': '编解码器注册和相关基类', 'datetime': '基础 日期 和 时间 数据类型', 'calendar': '日历相关函数', 'collections': '容器数据类型', 'heapq': '堆队列算法', 'bisect': '数组二分查找算法', 'array': 'Efficient arrays of numeric values', 'weakref': '弱引用', 'types': 'Dynamic type creation and names for built-in types', 'copy': '浅层 (shallow) 和深层 (deep) 复制操作', 'pprint': '数据美化输出', 'reprlib': 'Alternate repr() implementation', 'enum': 'Support for enumerations', 'numbers': '数字的抽象基类', 'math': '数学函数', 'decimal': '十进制定点和浮点运算', 'fractions': '分数', 'random': '生成伪随机数', 'statistics': 'Mathematical statistics functions', 'itertools': '为高效循环而创建迭代器的函数', 'functools': '高阶函数和可调用对象上的操作', 'operator': '标准运算符替代函数', 'pathlib': '面向对象的文件系统路径', 'fileinput': 'Iterate over lines from multiple input streams', 'stat': 'Interpreting stat() results', 'filecmp': '文件及目录的比较', 'tempfile': 'Generate temporary files and directories', 'glob': 'Unix style pathname pattern expansion', 'fnmatch': 'Unix filename pattern matching', 'linecache': 'Random access to text lines', 'shutil': 'High-level file operations', 'macpath': 'Mac OS 9 路径操作函数', 'copyreg': 'Register pickle support functions', 'shelve': 'Python object persistence', 'marshal': 'Internal Python object serialization', 'dbm': 'Interfaces to Unix "databases"', 'zlib': '与 gzip 兼容的压缩', 'gzip': '对 gzip 格式的支持', 'bz2': '对 bzip2 压缩算法的支持', 'lzma': '用 LZMA 算法压缩', 'zipfile': '使用ZIP存档', 'tarfile': '读写tar归档文件', 'csv': 'CSV 文件读写', 'configparser': 'Configuration file parser', 'netrc': 'netrc file processing', 'xdrlib': 'Encode and decode XDR data', 'hashlib': '安全哈希与消息摘要', 'hmac': '基于密钥的消息验证', 'secrets': 'Generate secure random numbers for managing secrets', 'os': '操作系统接口模块', 'io': '处理流的核心工具', 'time': '时间的访问和转换', 'argparse': '命令行选项、参数和子命令解析器', 'getopt': 'C-style parser for command line options', 'logging': 'Python 的日志记录工具', 'getpass': '便携式密码输入工具', 'curses': '终端字符单元显示的处理', 'platform': '获取底层平台的标识数据', 'errno': 'Standard errno system symbols', 'ctypes': 'Python 的外部函数库', 'threading': '基于线程的并行', 'multiprocessing': '基于进程的并行', 'subprocess': '子进程管理', 'sched': '事件调度器', 'queue': '一个同步的队列类', 'dummy_threading': '可直接替代 threading 模块。', 'contextvars': 'Context Variables', 'asyncio': '异步 I/O', 'socket': '底层网络接口', 'ssl': 'TLS/SSL wrapper for socket objects', 'select': 'Waiting for I/O completion', 'selectors': '高级 I/O 复用库', 'asyncore': '异步socket处理器', 'asynchat': '异步 socket 指令/响应 处理器', 'signal': '设置异步事件处理程序', 'mmap': '内存映射文件支持', 'email': '电子邮件与 MIME 处理包', 'json': 'JSON 编码和解码器', 'mailcap': 'Mailcap file handling', 'mailbox': 'Manipulate mailboxes in various formats', 'mimetypes': 'Map filenames to MIME types', 'base64': 'Base16, Base32, Base64, Base85 数据编码', 'binhex': '对binhex4文件进行编码和解码', 'binascii': '二进制和 ASCII 码互转', 'quopri': 'Encode and decode MIME quoted-printable data', 'uu': 'Encode and decode uuencode files', 'html': '超文本标记语言支持', 'webbrowser': '方便的Web浏览器控制器', 'cgi': 'Common Gateway Interface support', 'cgitb': 'Traceback manager for CGI scripts', 'wsgiref': 'WSGI Utilities and Reference Implementation', 'urllib': 'URL 处理模块', 'http': 'HTTP 模块', 'ftplib': 'FTP protocol client', 'poplib': 'POP3 protocol client', 'imaplib': 'IMAP4 protocol client', 'nntplib': 'NNTP protocol client', 'smtplib': 'SMTP协议客户端', 'smtpd': 'SMTP Server', 'telnetlib': 'Telnet client', 'uuid': 'UUID objects according to RFC 4122', 'socketserver': 'A framework for network servers', 'xmlrpc': 'XMLRPC 服务端与客户端模块', 'ipaddress': 'IPv4/IPv6 manipulation library', 'audioop': 'Manipulate raw audio data', 'aifc': 'Read and write AIFF and AIFC files', 'sunau': '读写 Sun AU 文件', 'wave': '读写WAV格式文件', 'chunk': 'Read IFF chunked data', 'colorsys': '颜色系统间的转换', 'imghdr': '推测图像类型', 'sndhdr': '推测声音文件的类型', 'ossaudiodev': 'Access to OSS-compatible audio devices', 'gettext': '多语种国际化服务', 'locale': '国际化服务', 'turtle': '海龟绘图', 'cmd': '支持面向行的命令解释器', 'shlex': 'Simple lexical analysis', 'tkinter': 'Tcl/Tk的Python接口', 'typing': '类型标注支持', 'pydoc': 'Documentation generator and online help system', 'doctest': '测试交互性的Python示例', 'unittest': '单元测试框架', '2to3': '自动将 Python 2 代码转为 Python 3 代码', 'test': 'Regression tests package for Python', 'bdb': 'Debugger framework', 'faulthandler': 'Dump the Python traceback', 'pdb': 'Python的调试器', 'timeit': '测量小代码片段的执行时间', 'trace': 'Trace or track Python statement execution', 'tracemalloc': 'Trace memory allocations', 'distutils': '构建和安装 Python 模块', 'ensurepip': 'Bootstrapping the pip installer', 'venv': '创建虚拟环境', 'zipapp': 'Manage executable Python zip archives', 'sys': '系统相关的参数和函数', 'sysconfig': "Provide access to Python's configuration information", 'builtins': '内建对象', 'warnings': 'Warning control', 'dataclasses': '数据类', 'contextlib': 'Utilities for with-statement contexts', 'abc': '抽象基类', 'atexit': '退出处理器', 'traceback': '打印或检索堆栈回溯', 'gc': '垃圾回收器接口', 'inspect': '检查对象', 'site': 'Site-specific configuration hook', 'code': 'Interpreter base classes', 'codeop': '编译Python代码', 'zipimport': 'Import modules from Zip archives', 'pkgutil': 'Package extension utility', 'modulefinder': '查找脚本使用的模块', 'runpy': 'Locating and executing Python modules', 'importlib': 'import 的实现', 'parser': 'Access Python parse trees', 'ast': '抽象语法树', 'symtable': "Access to the compiler's symbol tables", 'symbol': '与 Python 解析树一起使用的常量', 'token': '与Python解析树一起使用的常量', 'keyword': '检验Python关键字', 'tokenize': 'Tokenizer for Python source', 'tabnanny': '模糊缩进检测', 'pyclbr': 'Python class browser support', 'py_compile': 'Compile Python source files', 'compileall': 'Byte-compile Python libraries', 'dis': 'Python 字节码反汇编器', 'pickletools': 'Tools for pickle developers', 'formatter': 'Generic output formatting', 'msilib': 'Read and write Microsoft Installer files', 'msvcrt': 'Useful routines from the MS VC++ runtime', 'winreg': 'Windows 注册表访问', 'winsound': 'Sound-playing interface for Windows', 'posix': 'The most common POSIX system calls', 'pwd': '用户密码数据库', 'spwd': 'The shadow password database', 'grp': 'The group database', 'crypt': 'Function to check Unix passwords', 'termios': 'POSIX style tty control', 'tty': '终端控制功能', 'pty': 'Pseudo-terminal utilities', 'fcntl': 'The fcntl and ioctl system calls', 'pipes': 'Interface to shell pipelines', 'resource': 'Resource usage information', 'nis': "Interface to Sun's NIS (Yellow Pages)"}
BUILTIN_ITEMS = [('string', '常见的字符串操作'), ('re', '正则表达式操作'), ('difflib', '计算差异的辅助工具'), ('textwrap', '文本自动换行与填充'), ('unicodedata', 'Unicode 数据库'), ('stringprep', '因特网字符串预备'), ('readline', 'GNU readline 接口'), ('rlcompleter', 'GNU readline 的补全函数'), ('struct', '将字节串解读为打包的二进制数据'), ('codecs', '编解码器注册和相关基类'), ('datetime', '基础 日期 和 时间 数据类型'), ('calendar', '日历相关函数'), ('collections', '容器数据类型'), ('heapq', '堆队列算法'), ('bisect', '数组二分查找算法'), ('array', 'Efficient arrays of numeric values'), ('weakref', '弱引用'), ('types', 'Dynamic type creation and names for built-in types'), ('copy', '浅层 (shallow) 和深层 (deep) 复制操作'), ('pprint', '数据美化输出'), ('reprlib', 'Alternate repr() implementation'), ('enum', 'Support for enumerations'), ('numbers', '数字的抽象基类'), ('math', '数学函数'), ('decimal', '十进制定点和浮点运算'), ('fractions', '分数'), ('random', '生成伪随机数'), ('statistics', 'Mathematical statistics functions'), ('itertools', '为高效循环而创建迭代器的函数'), ('functools', '高阶函数和可调用对象上的操作'), ('operator', '标准运算符替代函数'), ('pathlib', '面向对象的文件系统路径'), ('fileinput', 'Iterate over lines from multiple input streams'), ('stat', 'Interpreting stat() results'), ('filecmp', '文件及目录的比较'), ('tempfile', 'Generate temporary files and directories'), ('glob', 'Unix style pathname pattern expansion'), ('fnmatch', 'Unix filename pattern matching'), ('linecache', 'Random access to text lines'), ('shutil', 'High-level file operations'), ('macpath', 'Mac OS 9 路径操作函数'), ('copyreg', 'Register pickle support functions'), ('shelve', 'Python object persistence'), ('marshal', 'Internal Python object serialization'), ('dbm', 'Interfaces to Unix "databases"'), ('zlib', '与 gzip 兼容的压缩'), ('gzip', '对 gzip 格式的支持'), ('bz2', '对 bzip2 压缩算法的支持'), ('lzma', '用 LZMA 算法压缩'), ('zipfile', '使用ZIP存档'), ('tarfile', '读写tar归档文件'), ('csv', 'CSV 文件读写'), ('configparser', 'Configuration file parser'), ('netrc', 'netrc file processing'), ('xdrlib', 'Encode and decode XDR data'), ('hashlib', '安全哈希与消息摘要'), ('hmac', '基于密钥的消息验证'), ('secrets', 'Generate secure random numbers for managing secrets'), ('os', '操作系统接口模块'), ('io', '处理流的核心工具'), ('time', '时间的访问和转换'), ('argparse', '命令行选项、参数和子命令解析器'), ('getopt', 'C-style parser for command line options'), ('logging', 'Python 的日志记录工具'), ('getpass', '便携式密码输入工具'), ('curses', '终端字符单元显示的处理'), ('platform', '获取底层平台的标识数据'), ('errno', 'Standard errno system symbols'), ('ctypes', 'Python 的外部函数库'), ('threading', '基于线程的并行'), ('multiprocessing', '基于进程的并行'), ('subprocess', '子进程管理'), ('sched', '事件调度器'), ('queue', '一个同步的队列类'), ('dummy_threading', '可直接替代 threading 模块。'), ('contextvars', 'Context Variables'), ('asyncio', '异步 I/O'), ('socket', '底层网络接口'), ('ssl', 'TLS/SSL wrapper for socket objects'), ('select', 'Waiting for I/O completion'), ('selectors', '高级 I/O 复用库'), ('asyncore', '异步socket处理器'), ('asynchat', '异步 socket 指令/响应 处理器'), ('signal', '设置异步事件处理程序'), ('mmap', '内存映射文件支持'), ('email', '电子邮件与 MIME 处理包'), ('json', 'JSON 编码和解码器'), ('mailcap', 'Mailcap file handling'), ('mailbox', 'Manipulate mailboxes in various formats'), ('mimetypes', 'Map filenames to MIME types'), ('base64', 'Base16, Base32, Base64, Base85 数据编码'), ('binhex', '对binhex4文件进行编码和解码'), ('binascii', '二进制和 ASCII 码互转'), ('quopri', 'Encode and decode MIME quoted-printable data'), ('uu', 'Encode and decode uuencode files'), ('html', '超文本标记语言支持'), ('webbrowser', '方便的Web浏览器控制器'), ('cgi', 'Common Gateway Interface support'), ('cgitb', 'Traceback manager for CGI scripts'), ('wsgiref', 'WSGI Utilities and Reference Implementation'), ('urllib', 'URL 处理模块'), ('http', 'HTTP 模块'), ('ftplib', 'FTP protocol client'), ('poplib', 'POP3 protocol client'), ('imaplib', 'IMAP4 protocol client'), ('nntplib', 'NNTP protocol client'), ('smtplib', 'SMTP协议客户端'), ('smtpd', 'SMTP Server'), ('telnetlib', 'Telnet client'), ('uuid', 'UUID objects according to RFC 4122'), ('socketserver', 'A framework for network servers'), ('xmlrpc', 'XMLRPC 服务端与客户端模块'), ('ipaddress', 'IPv4/IPv6 manipulation library'), ('audioop', 'Manipulate raw audio data'), ('aifc', 'Read and write AIFF and AIFC files'), ('sunau', '读写 Sun AU 文件'), ('wave', '读写WAV格式文件'), ('chunk', 'Read IFF chunked data'), ('colorsys', '颜色系统间的转换'), ('imghdr', '推测图像类型'), ('sndhdr', '推测声音文件的类型'), ('ossaudiodev', 'Access to OSS-compatible audio devices'), ('gettext', '多语种国际化服务'), ('locale', '国际化服务'), ('turtle', '海龟绘图'), ('cmd', '支持面向行的命令解释器'), ('shlex', 'Simple lexical analysis'), ('tkinter', 'Tcl/Tk的Python接口'), ('typing', '类型标注支持'), ('pydoc', 'Documentation generator and online help system'), ('doctest', '测试交互性的Python示例'), ('unittest', '单元测试框架'), ('2to3', '自动将 Python 2 代码转为 Python 3 代码'), ('test', 'Regression tests package for Python'), ('bdb', 'Debugger framework'), ('faulthandler', 'Dump the Python traceback'), ('pdb', 'Python的调试器'), ('timeit', '测量小代码片段的执行时间'), ('trace', 'Trace or track Python statement execution'), ('tracemalloc', 'Trace memory allocations'), ('distutils', '构建和安装 Python 模块'), ('ensurepip', 'Bootstrapping the pip installer'), ('venv', '创建虚拟环境'), ('zipapp', 'Manage executable Python zip archives'), ('sys', '系统相关的参数和函数'), ('sysconfig', "Provide access to Python's configuration information"), ('builtins', '内建对象'), ('warnings', 'Warning control'), ('dataclasses', '数据类'), ('contextlib', 'Utilities for with-statement contexts'), ('abc', '抽象基类'), ('atexit', '退出处理器'), ('traceback', '打印或检索堆栈回溯'), ('gc', '垃圾回收器接口'), ('inspect', '检查对象'), ('site', 'Site-specific configuration hook'), ('code', 'Interpreter base classes'), ('codeop', '编译Python代码'), ('zipimport', 'Import modules from Zip archives'), ('pkgutil', 'Package extension utility'), ('modulefinder', '查找脚本使用的模块'), ('runpy', 'Locating and executing Python modules'), ('importlib', 'import 的实现'), ('parser', 'Access Python parse trees'), ('ast', '抽象语法树'), ('symtable', "Access to the compiler's symbol tables"), ('symbol', '与 Python 解析树一起使用的常量'), ('token', '与Python解析树一起使用的常量'), ('keyword', '检验Python关键字'), ('tokenize', 'Tokenizer for Python source'), ('tabnanny', '模糊缩进检测'), ('pyclbr', 'Python class browser support'), ('py_compile', 'Compile Python source files'), ('compileall', 'Byte-compile Python libraries'), ('dis', 'Python 字节码反汇编器'), ('pickletools', 'Tools for pickle developers'), ('formatter', 'Generic output formatting'), ('msilib', 'Read and write Microsoft Installer files'), ('msvcrt', 'Useful routines from the MS VC++ runtime'), ('winreg', 'Windows 注册表访问'), ('winsound', 'Sound-playing interface for Windows'), ('posix', 'The most common POSIX system calls'), ('pwd', '用户密码数据库'), ('spwd', 'The shadow password database'), ('grp', 'The group database'), ('crypt', 'Function to check Unix passwords'), ('termios', 'POSIX style tty control'), ('tty', '终端控制功能'), ('pty', 'Pseudo-terminal utilities'), ('fcntl', 'The fcntl and ioctl system calls'), ('pipes', 'Interface to shell pipelines'), ('resource', 'Resource usage information'), ('nis', "Interface to Sun's NIS (Yellow Pages)")]
# @cache_page(None)
def module_list(request):
	# 这个页面不变永久缓存
	return render(request,'card/module_list.html',{'modules':BUILTIN_ITEMS})

def module_detail(request,module):
	"""模块细节视图"""
	if module not in BUILTINS.keys():
		return HttpResponse('No module names %s' % module)

	# 从缓存里拿数据
	context = cache.get(module+'_detail')
	if not context:
		a = __import__(module)
		fn = getattr(a,'__file__',None)
		if fn:
			with open(fn,'r') as f:
				fn = f.read()

		_dict = list(filter(lambda x:not x.startswith('_'),dir(a)))
		_all = getattr(a,'__all__',_dict)
		_all.sort()

		context={
			'name':getattr(a,'__name__',None),
			'doc':getattr(a,'__doc__',None),
			'all':_all,
			'file':fn,
		}
		cache.set(module+'_detail',context)
		cache.set(module+'_views',40)

	# 访问量加1
	watch = cache.incr(module+'_views',1)
	context['watch'] = watch

	return render(request, 'card/code.html', context)




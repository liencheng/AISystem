本文件夹的目的：
v1:20250630
由C++工程生成PFAI.exe，方便快速启动exe来调试
v2:20250710
1.依然可以通过生成exe来调试PFAI的C++工程。其实也可以直接在vs工程调试。
2.支持生成DLL并用于Unity工程（放到Plugins目录）

DLL说明：
可以通过修改C++工程属性及宏定义MYDLL_EXPORT来生成dll，生成路径建议改成PFAI\PFClient\Client\Assets\Plugins，
这样可以在Unity工程调用DLL。

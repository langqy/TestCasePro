// The following ifdef block is the standard way of creating macros which make exporting 
// from a DLL simpler. All files within this DLL are compiled with the TCP_DLL_EXPORTS
// symbol defined on the command line. This symbol should not be defined on any project
// that uses this DLL. This way any other project whose source files include this file see 
// TCP_DLL_API functions as being imported from a DLL, whereas this DLL sees symbols
// defined with this macro as being exported.
#ifdef TCP_DLL_EXPORTS
#define TCP_DLL_API __declspec(dllexport)
#else
#define TCP_DLL_API __declspec(dllimport)
#endif
#include<string>  
#include<windows.h>  
#include<vector>  
using namespace std ;
#include<assert.h>

#pragma pack(push)
#pragma pack(1)

extern "C" TCP_DLL_API int TCP_OpenConnection(char *ip_str,int port,unsigned int *connect_id) ;
extern "C" TCP_DLL_API void TCP_CloseConnection(unsigned int connect_id) ;
extern "C" TCP_DLL_API int TCP_SendData(unsigned int connect_id,char *buf,int len) ;
extern "C" TCP_DLL_API int TCP_RecieveData(unsigned int connect_id,char *recvBuf,int len,long timeout) ;

extern "C" TCP_DLL_API int HiLab_OpenDataQueryConnection(char *ip_str,int port,unsigned int *connect_id) ;
extern "C" TCP_DLL_API void HiLab_CloseDataQueryConnection(unsigned int connect_id) ;
extern "C" TCP_DLL_API int HiLab_GetQueryData(unsigned int connect_id,double *recvdat,int *len,long timeout) ;
extern "C" TCP_DLL_API int HiLab_RegisterDataQueryChannels(unsigned int connect_id,unsigned char Frequency,bool CaseSensitive,char *ChannelPaths,int len[],int index[],int *size);
extern "C" TCP_DLL_API int HiLab_GetData(char *ip_str,int port,char *ChannelPaths,char *Value) ;
extern "C" TCP_DLL_API int HiLab_SetData(char *ip_str,int port,char *ChannelPaths,int Priority,char *Value) ;
extern "C" TCP_DLL_API int Model_GetParameter(char *ip_str,int port, char *ModelName, char *Parameter, char *Value) ;
extern "C" TCP_DLL_API int Model_SetParameter(char *ip_str,int port, char *ModelName, char *Parameter, char *Value) ;
extern "C" TCP_DLL_API int HiLab_ClearDataHandle(char *ip_str,int port, char *ChannelPath) ;

#pragma pack(pop)
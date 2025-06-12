// export.cpp
#include <string>
#include <cstring>
#include "../Scene/AI/AIBehavior/AIBPatrol.h"
#include "../Scene/Obj/Obj_Char.h"
#include "../Scene/AI/AIPolicy/IPolicy.h"

extern "C"
{

    // ��������
    __declspec(dllexport)
        void* Behavior_Create(void* pChar)
    {
        Obj_Char* pObjChar = static_cast<Obj_Char*>(pChar);
        if (pObjChar == nullptr)
            return nullptr;
        AIBPatrol* pBehavior = new AIBPatrol(pObjChar);
        return static_cast<void*>(pBehavior);
    }

    // ���ٶ���
    __declspec(dllexport)
        void Behavior_Destroy(void
            * instance) {
        //delete from iPolicy
    }

    // ��ȡ��Ϣ
    __declspec(dllexport)
        const char* IPolicy_GetInfo(void
            * instance) {
        /*
        static
            std::string result;
        result =
            static_cast<IPolicy*>(instance)->GetInfo
            ();
        return result.c_str(); // ע�⣺���ص��Ǿ�̬�ַ������̲߳���ȫ��
        */
        return "";
    }

    // �޸���Ϣ
    __declspec(dllexport)
        void IPolicy_ChangeInfo(void* instance, int
            age) {
        /*
        static_cast<Person*>(instance)->SetAge
        (age);
        */
    }

}
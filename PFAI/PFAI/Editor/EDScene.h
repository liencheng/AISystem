#pragma once
#include "Public.h"
#include "../Scene/Obj/Obj_Char.h"
#include "../Scene/Obj/Obj_NPC.h"
#include "../Scene/Obj/Obj_Player.h"

using NPCVector = std::vector<Obj_NPC*>;
using PlayerVector = std::vector<Obj_Player*>;
using CharVector = std::vector<Obj_Char*>;

class EDScene: public Scene
{
public:
	EDScene();
	~EDScene();
public:
	void Init();
	void Update(float deltaTime);
	void Render();
	void Release();

	void AddChar(Obj_Char* pChar);
	void RemoveChar(Obj_Char* pChar);

private:
	CharVector m_Chars;

};

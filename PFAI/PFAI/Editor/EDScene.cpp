#include "EDScene.h"

EDScene::EDScene()
{
	Release();
}
EDScene::~EDScene()
{
	Release();
}
void EDScene::Init()
{
	// Initialize the scene, load resources, etc.
}
void EDScene::Release()
{
	CharVector::iterator it;
	for (it = m_Chars.begin(); it != m_Chars.end();)
	{
		if (*it)
		{
			delete* it; // Delete the character object
			*it = nullptr; // Set the pointer to nullptr to avoid dangling pointers
			it = m_Chars.erase(it); // Remove the element from the vector and decrement iterator
		}
		else
		{
			it = m_Chars.erase(it); // Remove the nullptr element
		}
	}
	// Release resources, clean up the scene.
}
void EDScene::Update(float deltaTime)
{
	for (auto& pChar : m_Chars)
	{
		if (pChar)
		{
			pChar->Update(deltaTime);
		}
	} 
}

void EDScene::Render()
{
	// Render the scene.
}

void EDScene::AddChar(Obj_Char* pChar)
{
	if (pChar)
	{
		m_Chars.push_back(pChar);
	}
}

void EDScene::RemoveChar(Obj_Char* pChar)
{
	auto it = std::remove(m_Chars.begin(), m_Chars.end(), pChar);
	if (it != m_Chars.end())
	{
		delete pChar;
		m_Chars.erase(it, m_Chars.end());
	}
}
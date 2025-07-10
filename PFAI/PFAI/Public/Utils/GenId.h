#pragma once
#include <cstdint>

enum class IdEnum
{
	ID_BEHAVIOR = 1,
	ID_GOALSENSOR = 2,
	ID_SIGNAL = 3,
};

#define ID_FACTOR (10000)

template<IdEnum T>
class GenId
{
public:
	GenId()
	{
		id = static_cast<int32_t>(T) * ID_FACTOR + 0;
	}
	// Generate a new unique ID
	int32_t generate() {
		return ++id;
	}

	int32_t id; // Current ID value
};

extern GenId<IdEnum::ID_BEHAVIOR> gGenBehaviorId;
extern GenId<IdEnum::ID_GOALSENSOR> gGenGoalId;
extern GenId<IdEnum::ID_SIGNAL> gGenSignalId;

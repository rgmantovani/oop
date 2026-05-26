// -----------------------------------------
// -----------------------------------------

enum Direction { North, South, East, West };

// -----------------------------------------
// -----------------------------------------

class MapSite {
    public:
        virtual void Enter() = 0;
};

// -----------------------------------------
// -----------------------------------------

class Room : public MapSite {
    public:
        Room (int roomNo) : roomNumber(roomNo) {}

        MapSite* GetSide(Direction dir) const {
            return sides[dir];
        }

        void SetSide(Direction dir, MapSite* mapSite) {
            sides[dir] = mapSite;
        }

        int GetRoomNumber() const {
            return roomNumber;
        }

        virtual void Enter() {}

    private:
        MapSite* sides[4];
        int roomNumber;
};

// -----------------------------------------
// -----------------------------------------

class Wall: public MapSite {
    public:
        Wall() {}
        virtual void Enter() {}
};

// -----------------------------------------
// -----------------------------------------

class Door: public MapSite {
    public:
        Door(Room* r1 = 0, Room* r2 = 0) : _room1(r1), _room2(r2) {}
        virtual void Enter() {}
        Room* OtherSideFrom(Room* room) {
            if (room == _room1) {
                return _room2;
            } else {
                return _room1;
            }
        }

        int IsOpen() const {
            return _isOpen;
        }

         void SetOpen(bool open) {
            _isOpen = open;
        }

    private:
        Room* _room1;
        Room* _room2;
        bool _isOpen;
};

// -----------------------------------------
// -----------------------------------------

class Maze {
    public:
        Maze() {}
        void AddRoom(Room* room) {
            rooms[room->GetRoomNumber()] = room;
        }
        Room* RoomNo(int roomNo) const {
            return rooms[roomNo];
        }

    private:
        Room* rooms[100];
};

// -----------------------------------------
// -----------------------------------------

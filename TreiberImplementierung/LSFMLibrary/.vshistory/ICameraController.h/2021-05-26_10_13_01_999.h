#pragma once

#include <windows.h>
#include <vector>


struct DataPack
{
	int width;
	int height;
	size_t buffersize;
	WORD* bufferptr;

};

struct DataPack_FLIM
{

	int width;
	int height;
	int imgNumber;
	WORD* bufferptr1 = NULL;
	WORD* bufferptr2 = NULL;
	WORD* bufferptr3 = NULL;
	WORD* bufferptr4 = NULL;
	WORD* bufferptr5 = NULL;
	WORD* bufferptr6 = NULL;
	WORD* bufferptr7 = NULL;
	WORD* bufferptr8 = NULL;
	WORD* bufferptr9 = NULL;
	WORD* bufferptr10 = NULL;
	WORD* bufferptr11 = NULL;
	WORD* bufferptr12 = NULL;
	WORD* bufferptr13 = NULL;
	WORD* bufferptr14 = NULL;
	WORD* bufferptr15 = NULL;
	WORD* bufferptr16 = NULL;
};
enum WaveForm
{
	sinusoidal = 1,
	rectangular = 2
};

enum PhaseNumber {
	Two = 1,
	Four = 2,
	Eight = 3,
	Sixteen = 4
};

enum PhaseSymmetry {
	singular = 0,
	twice = 1
};

enum PhaseOrder {
	ascending = 0,
	opposite = 1
};

enum TapSelect {
	both = 0,
	Tap_A = 1,
	Tap_B = 2
};

enum CameraTyp {
	LSFM = 0,
	LSFM_FLIM = 1
};

class ICameraController
{
public:
	virtual ~ICameraController() {}
	virtual std::vector<WORD*> SingleImageAquisition(int cameraTyp, HANDLE recorder, HANDLE camera, int phaseNumber, int phasesymmetry, int tapSelect, char* file_name, int* imgWidth, int* imgHeight) = 0;
	virtual  void GetExposureAndDelayTime(HANDLE camera, WORD* expousreTime, WORD* delay) = 0;
	virtual void SetExposureTime(HANDLE camera, DWORD exposureTime, DWORD delay) = 0;
	virtual DataPack* Live_View(int cameraTyp, HANDLE camera, HANDLE recorder) = 0;
	virtual void Start_Sequence(HANDLE camera) = 0;
	virtual void GetCameraAndRecorderHandle(HANDLE* camera, HANDLE* recorder) = 0;
	virtual bool SetFilmPhaseSequenceParameter(PhaseNumber phaseNumber, PhaseSymmetry phasesymmetry, PhaseOrder phaseOrder, TapSelect tapSelect) = 0;
	virtual long int Get_Camera_Modulation_Frequency() = 0;
	virtual bool Set_Camera_Modulation_Frequency(DWORD waveform) = 0;
	virtual bool GetFilmPhaseSequenceParameter(PhaseNumber* phaseNumber, PhaseSymmetry* phasesymmetry, PhaseOrder* phaseOrder, TapSelect* tapSelect) = 0;
	virtual bool GetCameraStatusConnection() = 0;
	virtual bool IsHardwareConnected() = 0;


};
#include <pybind11/pybind11.h>

// pybind11/stl.h:
// may be required to take into account ImGuiIO::std::string IniFilename
// (the wheel fails whenever we include it or not)
#include <pybind11/stl.h>


#include "imgui.h"
#include "imgui_internal.h"

namespace py = pybind11;

//
// We have to import private declarations from imgui.cpp, in order to be able to
// bind ImGuiContext. Below are verbatim copies of 3 structs from imgui.cpp:
// ImGuiDockRequestType, ImGuiDockRequest, ImGuiDockNodeSettings
// (minus the constructors implementations)

enum ImGuiDockRequestType
{
    ImGuiDockRequestType_None = 0,
    ImGuiDockRequestType_Dock,
    ImGuiDockRequestType_Undock,
    ImGuiDockRequestType_Split                  // Split is the same as Dock but without a DockPayload
};

struct ImGuiDockRequest
{
    ImGuiDockRequestType    Type;
    ImGuiWindow*            DockTargetWindow;   // Destination/Target Window to dock into (may be a loose window or a DockNode, might be NULL in which case DockTargetNode cannot be NULL)
    ImGuiDockNode*          DockTargetNode;     // Destination/Target Node to dock into
    ImGuiWindow*            DockPayload;        // Source/Payload window to dock (may be a loose window or a DockNode), [Optional]
    ImGuiDir                DockSplitDir;
    float                   DockSplitRatio;
    bool                    DockSplitOuter;
    ImGuiWindow*            UndockTargetWindow;
    ImGuiDockNode*          UndockTargetNode;

    ImGuiDockRequest();
//    {
//        Type = ImGuiDockRequestType_None;
//        DockTargetWindow = DockPayload = UndockTargetWindow = NULL;
//        DockTargetNode = UndockTargetNode = NULL;
//        DockSplitDir = ImGuiDir_None;
//        DockSplitRatio = 0.5f;
//        DockSplitOuter = false;
//    }
};

struct ImGuiDockNodeSettings
{
    ImGuiID             ID;
    ImGuiID             ParentNodeId;
    ImGuiID             ParentWindowId;
    ImGuiID             SelectedTabId;
    signed char         SplitAxis;
    char                Depth;
    ImGuiDockNodeFlags  Flags;                  // NB: We save individual flags one by one in ascii format (ImGuiDockNodeFlags_SavedFlagsMask_)
    ImVec2ih            Pos;
    ImVec2ih            Size;
    ImVec2ih            SizeRef;
    ImGuiDockNodeSettings();
    //ImGuiDockNodeSettings() { memset(this, 0, sizeof(*this)); SplitAxis = ImGuiAxis_None; }
};




void py_init_module_imgui(py::module& m)
{
    m.def("create_context",
          ImGui::CreateContext,
          pybind11::return_value_policy::reference);

    auto pyClassImGuiContext =
        py::class_<ImGuiContext>
            (m, "Context", "")
            .def(py::init<ImFontAtlas *>(),
                 py::arg("shared_font_atlas"))
    ;

    auto pyClassImGuiFontAtlas =
        py::class_<ImFontAtlas>
            (m, "FontAtlas", "")
            .def(py::init<>())
    ;

}

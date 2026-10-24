import { BrowserRouter, Navigate, Route, Routes } from 'react-router'
import { ProblemDatabasePage } from './features/problem-database'
import { TopicTreePage } from './features/topic-tree'
import { PROBLEMS_PATH, TREE_PATH } from './shared/routes'
import { WithSidebar } from './Sidebar'

// The app shell: the sidebar with the navigation on the left (a row on top on narrow screens) and the
// current page filling the rest of the window. Pages scroll inside themselves, never the window. Each
// tool lives in its own folder under features/ and is only given an address here and a link in the sidebar.
function App() {
  return (
    <BrowserRouter>
      <WithSidebar>
        <Routes>
          <Route path={TREE_PATH} element={<TopicTreePage />} />
          <Route path={PROBLEMS_PATH} element={<ProblemDatabasePage />} />
          <Route path="*" element={<Navigate to={TREE_PATH} replace />} />
        </Routes>
      </WithSidebar>
    </BrowserRouter>
  )
}

export default App

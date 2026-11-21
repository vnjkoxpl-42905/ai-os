import { cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { MemoryRouter, useLocation } from 'react-router-dom';
import { afterEach, expect, it } from 'vitest';
import { OPENING_COURSE_PATH } from '../openingCoursePath';
import { OpeningCourseNavigation, OpeningCourseScreen } from './OpeningCourse';

const url = (id: string, run = false) => `/course/${id}${run ? '?run=1' : ''}`;
afterEach(cleanup);

it('offers nine dedicated notes and four interleaved drill entries', () => {
  render(<MemoryRouter><OpeningCourseScreen url={url}/></MemoryRouter>);
  const list = screen.getByRole('list');
  expect(within(list).getAllByRole('listitem')).toHaveLength(13);
  expect(screen.getAllByRole('link', { name: /Read lesson/ })).toHaveLength(9);
  expect(screen.getAllByRole('link', { name: /View drill/ })).toHaveLength(4);
  expect(document.querySelector('.co-pages')).toBeNull();
  expect(OPENING_COURSE_PATH.slice(0, 4).map(step => step.id)).toEqual(['meaning', 'sufficient', 'necessary', 'foundation-practice']);
});

it.each(OPENING_COURSE_PATH)('renders the dedicated $id destination without an old reader index', async step => {
  render(<MemoryRouter><OpeningCourseScreen view={step.id} run={step.type === 'drill'} url={url}/></MemoryRouter>);
  expect(screen.getByRole('heading', { level: 1, name: step.title })).toBeVisible();
  await waitFor(() => expect(document.querySelector('.opening-course-content')).not.toBeNull());
  expect(document.querySelector('.co-pages')).toBeNull();
  expect(screen.getByRole('navigation', { name: 'Course navigation' })).toBeVisible();
  expect(screen.queryByRole('button', { name: /Mark lesson/ })).toBeNull();
});

it('separates a drill landing from its attempt surface', () => {
  const { rerender } = render(<MemoryRouter><OpeningCourseScreen view="foundation-practice" url={url}/></MemoryRouter>);
  expect(screen.getByRole('link', { name: 'Start drill' })).toHaveAttribute('href', '/course/foundation-practice?run=1');
  expect(screen.queryByRole('button', { name: 'Yes, it says I win.' })).toBeNull();
  rerender(<MemoryRouter><OpeningCourseScreen view="foundation-practice" run url={url}/></MemoryRouter>);
  expect(screen.getByRole('button', { name: 'Yes, it says I win.' })).toBeVisible();
});

it('retains a corrected answer when returning from another dedicated lesson', () => {
  const { rerender } = render(<MemoryRouter><OpeningCourseScreen view="meaning" url={url}/></MemoryRouter>);
  fireEvent.click(screen.getByRole('button', { name: 'Yes, it says I win.' }));
  expect(screen.getByText('Not quite.')).toBeVisible();
  fireEvent.click(screen.getByRole('button', { name: 'No, it tells me what follows if I win.' }));
  rerender(<MemoryRouter><OpeningCourseScreen view="sufficient" url={url}/></MemoryRouter>);
  expect(screen.queryByRole('button', { name: 'No, it tells me what follows if I win.' })).toBeNull();
  rerender(<MemoryRouter><OpeningCourseScreen view="meaning" url={url}/></MemoryRouter>);
  expect(screen.getByRole('button', { name: 'No, it tells me what follows if I win.' })).toHaveAttribute('aria-pressed', 'true');
  expect(screen.getByText('Correct.')).toBeVisible();
});

it('exposes only the permitted content and flashcard families', () => {
  const steps = OPENING_COURSE_PATH.filter(step => step.unitId === 'group-1');
  const { rerender } = render(<MemoryRouter><OpeningCourseScreen view="necessary" steps={steps} url={url}/></MemoryRouter>);
  expect(screen.getByRole('heading', { name: 'This lesson is not available here.' })).toBeVisible();
  expect(document.querySelector('.opening-course-content')).toBeNull();
  rerender(<MemoryRouter><OpeningCourseScreen view="tools" steps={steps} url={url}/></MemoryRouter>);
  expect(screen.getByRole('heading', { name: 'Sufficient-condition words' })).toBeVisible();
  expect(screen.queryByRole('heading', { name: 'Necessary-condition words' })).toBeNull();
});


function CourseNavigationHarness() {
  const location = useLocation();
  const view = location.pathname.split('/').pop() || 'lessons';
  return <><OpeningCourseNavigation view={view} url={url}/><OpeningCourseScreen view={view} url={url}/></>;
}

it('focuses the destination after drawer navigation and restores the trigger after Escape', async () => {
  render(<MemoryRouter initialEntries={['/course/meaning']}><CourseNavigationHarness/></MemoryRouter>);
  fireEvent.click(screen.getByRole('button', { name: 'Course menu' }));
  fireEvent.click(within(screen.getByRole('dialog')).getByRole('link', { name: 'Lessons' }));
  await waitFor(() => expect(screen.queryByRole('dialog')).toBeNull());
  await waitFor(() => expect(screen.getByRole('heading', { level: 1, name: 'Conditional reasoning.' })).toHaveFocus());
  fireEvent.click(screen.getByRole('button', { name: 'Course menu' }));
  fireEvent.keyDown(screen.getByRole('dialog'), { key: 'Escape' });
  await waitFor(() => expect(screen.queryByRole('dialog')).toBeNull());
  await waitFor(() => expect(screen.getByRole('button', { name: 'Course menu' })).toHaveFocus());
});
